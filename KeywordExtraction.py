"""
Keyword Extraction Tool (Streamlit + Gensim)

How to run:
    pip install streamlit
    pip install gensim
    streamlit run KeywordExtraction.py

This simple app lets you paste a block of text and extract keywords
using gensim.summarization.keywords.

File: KeywordExtraction.py
"""

import streamlit as st

# Try to import the legacy gensim summarization keywords module.
# Newer versions of gensim (>=4) removed this module, so we handle
# the ImportError gracefully and provide a modern fallback (YAKE).
try:
    from gensim.summarization import keywords as gensim_keywords
    GENSIM_AVAILABLE = True
except Exception:
    gensim_keywords = None
    GENSIM_AVAILABLE = False

# Try to import YAKE (Yet Another Keyword Extractor) as a fallback.
# YAKE is pure-Python and works on modern Python versions.
try:
    import yake
    YAKE_AVAILABLE = True
except Exception:
    yake = None
    YAKE_AVAILABLE = False


def extract_keywords(text):
    """Extract keywords from a block of text using gensim.

    Args:
        text (str): The input text to extract keywords from.

    Returns:
        list[str]: A list of extracted keywords (may be empty).

    Notes:
        - Uses gensim.summarization.keywords with split=True to return a list.
        - This function does not use Streamlit directly so it can be unit tested.
    """
    # Guard against empty input
    if not text or not text.strip():
        return []

    # Prefer gensim.summarization if available (keeps original behavior).
    if GENSIM_AVAILABLE:
        kw_list = gensim_keywords(text, split=True, lemmatize=True)
        return [str(k).strip() for k in kw_list if k and str(k).strip()]

    # Otherwise, try YAKE as a modern fallback.
    if YAKE_AVAILABLE:
        # Use YAKE to extract keywords. We pick a reasonable default:
        # - language: English
        # - max_ngram_size: 3 (allow up to 3-word keywords)
        # - top N keywords: return top 20 (then filter empty)
        kw_extractor = yake.KeywordExtractor(lan="en", n=3, top=20)
        yake_keywords = kw_extractor.extract_keywords(text)
        # yake returns list of (keyword, score); we extract the keyword text
        kw_list = [k for k, score in yake_keywords]
        return [str(k).strip() for k in kw_list if k and str(k).strip()]

    # If neither extractor is available, raise an informative error
    raise ImportError(
        "No keyword extraction backend is available.\n"
        "Install YAKE via `pip install yake` or install a compatible gensim."
    )


def main():
    """Streamlit UI entry point."""
    # App title and short description
    st.title("Keyword Extraction Tool")
    st.write("Paste text below and click 'Extract Keywords' to get keywords using gensim.")

    # Multiline text input area for the user
    text = st.text_area("Enter or paste your text here:", height=240)

    # When the button is clicked, attempt extraction
    if st.button("Extract Keywords"):
        # If no text is provided, show a warning
        if not text or not text.strip():
            st.warning("Please enter some text before extracting keywords.")
            return

        # Show a small spinner while extracting
        with st.spinner("Extracting keywords..."):
            kw_list = extract_keywords(text)

        # Display results
        if not kw_list:
            st.info("No keywords could be extracted from the provided text.")
        else:
            st.subheader("Extracted Keywords")
            # Display each keyword on its own line for clarity
            for kw in kw_list:
                st.write("- " + kw)

            # Also show a compact, comma-separated view
            st.markdown("**Keywords (comma-separated):** " + ", ".join(kw_list))


if __name__ == "__main__":
    main()
