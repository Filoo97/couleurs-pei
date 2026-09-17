from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")


class PriorityWebsiteFixesTests(unittest.TestCase):
    def test_samoussa_description_respects_confirmed_origin(self):
        description = re.search(
            r"<h3>Samoussas</h3>\s*<p>(.*?)</p>", INDEX, re.DOTALL
        ).group(1)
        self.assertNotIn("maison", description.lower())
        self.assertIn("Réunion", description)

    def test_generic_hours_do_not_contradict_location_schedule(self):
        self.assertNotIn("Midi 11h30 - 14h00 / Soir 18h30 - 21h00", INDEX)
        self.assertNotIn("Mardi - Samedi", INDEX)
        self.assertIn("Consultez le planning", INDEX)

    def test_footer_links_to_the_confirmed_facebook_page(self):
        self.assertIn('href="https://www.facebook.com/108411414051929"', INDEX)

    def test_legacy_meta_scripts_do_not_embed_an_access_token(self):
        for relative_path in (
            "Marketing/Scripts/get_ig_id.py",
            "Marketing/Scripts/publish_api.py",
        ):
            source = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIsNone(re.search(r'ACCESS_TOKEN\s*=\s*["\']', source))
            self.assertIn("os.environ", source)

    def test_mobile_quick_actions_offer_planning_call_and_traiteur_paths(self):
        self.assertIn('class="quick-actions"', INDEX)
        self.assertIn('href="#planning"', INDEX)
        self.assertIn('class="protected-phone quick-action"', INDEX)
        self.assertIn('href="#reservation"', INDEX)

    def test_traiteur_section_uses_only_confirmed_event_types(self):
        self.assertIn('id="traiteur"', INDEX)
        for label in ("Anniversaire", "Baptême", "Repas de famille", "Événement professionnel"):
            self.assertIn(label, INDEX)

    def test_non_hero_images_are_lazy_loaded(self):
        self.assertIn('src="samoussa.png" alt="Samoussas" loading="lazy"', INDEX)
        self.assertIn('src="cgss-reunion.jpg" alt="CGSS de la Réunion" loading="lazy"', INDEX)

    def test_primary_navigation_includes_a_skip_link(self):
        self.assertIn('class="skip-link" href="#main-content"', INDEX)
        self.assertIn('<main id="main-content">', INDEX)


if __name__ == "__main__":
    unittest.main()
