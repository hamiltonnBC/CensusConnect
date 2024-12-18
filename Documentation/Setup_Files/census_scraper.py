import logging
from bs4 import BeautifulSoup
from typing import List, Dict

def setup_logging():
    """
    Set up logging configuration with DEBUG level to see everything.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

class CensusLabelParser:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def extract_all_spans(self, html_content: str) -> List[str]:
        """
        Extract all span contents to verify what we're finding.

        Args:
            html_content: Raw HTML string

        Returns:
            List[str]: All span contents found
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        spans = []

        # Find all ag-group-value spans first
        value_spans = soup.find_all('span', class_='ag-group-value')

        for span in value_spans:
            # Get the inner span
            inner_span = span.find('span')
            if inner_span and inner_span.text.strip():
                spans.append(inner_span.text.strip())
                self.logger.debug(f"Found label: {inner_span.text.strip()}")

        return spans

    def build_hierarchy(self, spans: List[str]) -> Dict:
        """
        Build hierarchical structure of labels.
        This is a placeholder for now - let's first verify we're finding all labels.

        Args:
            spans: List of span contents

        Returns:
            Dict: Hierarchical structure
        """
        return {"labels": spans}

def main():
    """
    Main function to extract and display all labels.
    """
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        # Initialize parser
        parser = CensusLabelParser()

        # Get test HTML content
        with open('census_page.html', 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Extract all spans first
        spans = parser.extract_all_spans(html_content)

        # Print everything we found
        logger.info("Found the following labels:")
        for i, span in enumerate(spans, 1):
            logger.info(f"{i}. {span}")

        logger.info(f"Total labels found: {len(spans)}")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()