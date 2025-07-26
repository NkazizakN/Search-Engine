import re
import pickle
input_dir = 'wsj.xml'
with open(input_dir, 'r') as file:
    journal = file.read()

documents = []
all_words = []
pattern = re.compile(r'<DOC>(.*?)</DOC>', re.DOTALL)
docs = pattern.findall(journal)

for doc in docs:
    ##gathering different tags that has information
    MS_extract = re.search(r'<MS>(.*?)</MS>', doc, re.DOTALL)
    GV_extract = re.search(r'<GV>(.*?)</GV>', doc, re.DOTALL)
    ST_extract = re.search(r'<ST>(.*?)</ST>', doc, re.DOTALL)
    NS_extract = re.search(r'<NS>(.*?)</NS>', doc, re.DOTALL)
    SO_extract = re.search(r'<SO>(.*?)</SO>', doc, re.DOTALL)
    AN_extract = re.search(r'<AN>(.*?)</AN>', doc, re.DOTALL)
    G_extract = re.search(r'<G>(.*?)</G>', doc, re.DOTALL)
    DOCNO_extract = re.search(r'<DOCNO>(.*?)</DOCNO>', doc, re.DOTALL)
    DATE_extract = re.search(r'<DATE>(.*?)</DATE>', doc, re.DOTALL)
    AUTHOR_extract = re.search(r'<AUTHOR>(.*?)</AUTHOR>', doc, re.DOTALL)
    RE_extract = re.search(r'<RE>(.*?)</RE>', doc, re.DOTALL)
    CO_extract = re.search(r'<CO>(.*?)</CO>', doc, re.DOTALL)
    DD_extract = re.search(r'<DD>(.*?)</DD>', doc, re.DOTALL)
    DATELINE_extract = re.search(r'<DATELINE>(.*?)</DATELINE>', doc, re.DOTALL)
    HL_extract = re.search(r'<HL>(.*?)</HL>', doc, re.DOTALL)
    IN_extract = re.search(r'<IN>(.*?)</IN>', doc, re.DOTALL)
    LP_extract = re.search(r'<LP>(.*?)</LP>', doc, re.DOTALL)
    TEXT_extract = re.search(r'<TEXT>(.*?)</TEXT>', doc, re.DOTALL)

    ##if any or all tags contains any viable information
    if DOCNO_extract and (HL_extract or IN_extract or LP_extract or TEXT_extract or DATELINE_extract or DD_extract):
        DOCNO = DOCNO_extract.group(1).strip()
        words_MS = []
        words_GV = []
        words_ST = []
        words_NS = []
        words_SO = []
        words_AN = []
        words_G = []
        words_HL = []
        words_IN = []
        words_LP = []
        words_TEXT = []
        words_DATE = []
        words_AUTHOR = []
        words_RE = []
        words_CO = []
        words_DD = []
        words_DATELINE = []

        # if the words
        if MS_extract:
            MS = MS_extract.group(1).strip()
            MS = re.sub(r'<.*?>', '', MS)
            words_MS = re.findall(r'\b\w+\b', MS.lower())
        if GV_extract:
            GV = GV_extract.group(1).strip()
            GV = re.sub(r'<.*?>', '', GV)
            words_GV = re.findall(r'\b\w+\b', GV.lower())
        if ST_extract:
            ST = ST_extract.group(1).strip()
            ST = re.sub(r'<.*?>', '', ST)
            words_ST = re.findall(r'\b\w+\b', ST.lower())
        if NS_extract:
            NS = NS_extract.group(1).strip()
            NS = re.sub(r'<.*?>', '', NS)
            words_NS = re.findall(r'\b\w+\b', NS.lower())
        if SO_extract:
            SO = SO_extract.group(1).strip()
            SO = re.sub(r'<.*?>', '', SO)
            words_SO = re.findall(r'\b\w+\b', SO.lower())
        if AN_extract:
            AN = AN_extract.group(1).strip()
            AN = re.sub(r'<.*?>', '', AN)
            words_AN = re.findall(r'\b\w+\b', AN.lower())
        if G_extract:
            G = G_extract.group(1).strip()
            G = re.sub(r'<.*?>', '', G)
            words_G = re.findall(r'\b\w+\b', G.lower())
        if DATE_extract:
            DATE = DATE_extract.group(1).strip()
            DATE = re.sub(r'<.*?>', '', DATE)
            words_DATE = re.findall(r'\b\w+\b', DATE.lower())
        if AUTHOR_extract:
            AUTHOR = AUTHOR_extract.group(1).strip()
            AUTHOR = re.sub(r'<.*?>', '', AUTHOR)
            words_AUTHOR = re.findall(r'\b\w+\b', AUTHOR.lower())
        if RE_extract:
            RE = RE_extract.group(1).strip()
            RE = re.sub(r'<.*?>', '', RE)
            words_RE = re.findall(r'\b\w+\b', RE.lower())
        if CO_extract:
            CO = CO_extract.group(1).strip()
            CO = re.sub(r'<.*?>', '', CO)
            words_CO = re.findall(r'\b\w+\b', CO.lower())
        if DD_extract:
            DD = str(DD_extract.group(1).strip())
            DD = re.sub(r'<.*?>', '', DD)
            words_DD = [DD]
        if HL_extract:
            HL = HL_extract.group(1).strip()
            HL = re.sub(r'<.*?>', '', HL)
            words_HL = re.findall(r'\b\w+\b', HL.lower())
        if DATELINE_extract:
            DATELINE = DATELINE_extract.group(1).strip()
            DATELINE = re.sub(r'<.*?>', '', DATELINE)
            words_DATELINE = re.findall(r'\b\w+\b', DATELINE.lower())
        if IN_extract:
            IN = IN_extract.group(1).strip()
            IN = re.sub(r'<.*?>', '', IN)
            words_IN = re.findall(r'\b\w+\b', IN.lower())
        if LP_extract:
            LP = LP_extract.group(1).strip()
            LP = re.sub(r'<.*?>', '', LP)
            words_LP = re.findall(r'\b\w+\b', LP.lower())
        if TEXT_extract:
            TEXT = TEXT_extract.group(1).strip()
            TEXT = re.sub(r'<.*?>', '', TEXT)
            words_TEXT = re.findall(r'\b\w+\b', TEXT.lower())
        words = words_HL + words_IN + words_LP + words_TEXT + words_DATELINE + words_DD + words_CO + words_RE
        words += words_MS + words_GV + words_ST + words_NS + words_SO + words_AN + words_G + words_AUTHOR + words_DATE
        documents.append((DOCNO, words))

# prepared file for the indexer to load
with open('for_indexer.pkl', 'wb') as file:
    pickle.dump(documents, file)

# output for the indexer code with each word in separate line
with open("Parser_output.txt", "w") as file:
    for docs in documents:
        for word in docs[1]:
            file.write(word + "\n")  # Write each word followed by a newline
        file.write("\n")  # blank line after each document
