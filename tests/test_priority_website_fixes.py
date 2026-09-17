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


if __name__ == "__main__":
    unittest.main()
