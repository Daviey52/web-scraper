# Web scraper

## Feature Task and Requirements

1. Scrape a Wikipedia page and record which passages need citations.
    .E.g. History of Mexico has a few “citations needed”.
2. Your web scraper should report the number of citations needed.
3. Your web scraper should identify those cases AND include the relevant passage.
    .E.g. Citation needed for “lorem spam and impsum eggs”
     .Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes

1. Count function must be named get_citations_needed_count
    .get_citations_needed takes in a url and returns an integer
2. Report function must be named get_citations_needed_report
   .get_citations_needed_report takes in a url and returns a string
   .the string should be formatted with each citation needed on own line, in order found.
3. Module must be named scraper.py
