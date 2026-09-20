from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
STYLE = (ROOT / "style.css").read_text(encoding="utf-8")


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
        self.assertIn('href="tel:0650844247" class="quick-action"', INDEX)
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

    def test_homepage_offers_two_clear_primary_paths(self):
        hero = re.search(r'<section id="accueil".*?</section>', INDEX, re.DOTALL).group(0)
        self.assertIn('class="hero-kicker"', hero)
        self.assertIn('class="hero-actions"', hero)
        self.assertIn('href="#planning"', hero)
        self.assertIn('href="#traiteur"', hero)
        self.assertLess(INDEX.index('<main id="main-content">'), INDEX.index('<section id="accueil"'))

    def test_location_schedule_is_a_semantic_list_with_confirmed_details(self):
        planning = re.search(r'<section id="planning".*?</section>', INDEX, re.DOTALL).group(0)
        self.assertIn('<ol class="location-list"', planning)
        self.assertEqual(planning.count('<li class="location-card'), 5)
        self.assertIn('18h00 - 21h00', planning)
        self.assertIn('11h45 - 14h00', planning)
        self.assertIn('Jeudi <span>soir</span>', planning)
        self.assertIn('<strong>Boussy-Saint-Antoine</strong><br>Place de la ferme', planning)
        self.assertIn('query=Place+de+la+ferme+Boussy-Saint-Antoine', planning)
        self.assertNotIn('Emplacement variable', planning)
        self.assertNotIn('confirmer par téléphone', planning)

    def test_footer_uses_the_current_year_and_mobile_menu_is_visible(self):
        self.assertIn('&copy; 2026 Couleurs Péï', INDEX)
        self.assertIn('.hamburger {', STYLE)
        self.assertIn('min-width: 48px;', STYLE)
        self.assertIn('background: var(--primary-color);', STYLE)

    def test_traiteur_path_explains_the_request_and_collects_key_details(self):
        traiteur = re.search(r'<section id="traiteur".*?</section>', INDEX, re.DOTALL).group(0)
        reservation = re.search(r'<section id="reservation".*?</section>', INDEX, re.DOTALL).group(0)
        self.assertIn('class="traiteur-steps"', traiteur)
        self.assertEqual(traiteur.count('<li>'), 3)
        for field_name in ('date_evenement', 'lieu_evenement', 'nombre_personnes'):
            self.assertIn(f'name="{field_name}"', reservation)
        self.assertIn('aria-live="polite"', reservation)
        self.assertNotIn('Réponse sous 24h', reservation)

    def test_navigation_controls_are_keyboard_accessible(self):
        self.assertIn('<button class="hamburger"', INDEX)
        self.assertIn('aria-controls="primary-navigation"', INDEX)
        self.assertIn('aria-expanded="false"', INDEX)
        self.assertIn('id="primary-navigation"', INDEX)
        self.assertIn("hamburger.setAttribute('aria-expanded'", INDEX)
        self.assertIn("event.key === 'Escape'", INDEX)

    def test_css_version_is_incremented_for_the_redesign(self):
        self.assertIn('href="style.css?v=10"', INDEX)

    def test_redesign_respects_brand_palette_and_reduced_motion(self):
        for color in ('#2c3a51', '#ba9669', '#cbd3e0', '#F9F9F9'):
            self.assertIn(color.lower(), STYLE.lower())
        self.assertIn('@media (prefers-reduced-motion: reduce)', STYLE)

    def test_cookie_choice_is_identified_and_compact_on_small_mobile_screens(self):
        self.assertIn('role="dialog"', INDEX)
        self.assertIn('aria-label="Préférences relatives aux cookies"', INDEX)
        self.assertIn('@media (max-width: 480px)', INDEX)


if __name__ == "__main__":
    unittest.main()
