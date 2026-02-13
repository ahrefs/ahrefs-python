# AUTO-GENERATED -- DO NOT EDIT

# ruff: noqa: E501

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from ahrefs.types._coercions import DateStr, SelectStr


class AggregationEnum(StrEnum):
    SIMILAR_LINKS = "similar_links"
    _1_PER_DOMAIN = "1_per_domain"
    ALL = "all"

class BestPositionKindEnum(StrEnum):
    PAID_TOP = "paid_top"
    PAID_BOTTOM = "paid_bottom"
    PAID_RIGHT = "paid_right"
    PAID_SITELINK = "paid_sitelink"
    ORGANIC = "organic"
    SITELINK = "sitelink"
    SNIPPET = "snippet"
    IMAGE = "image"
    ARTICLE = "article"
    KNOWLEDGE_CARD = "knowledge_card"
    KNOWLEDGE_PANEL = "knowledge_panel"
    LOCAL_PACK = "local_pack"
    LOCAL_TEASER = "local_teaser"
    NEWS = "news"
    QUESTION = "question"
    REVIEW = "review"
    SHOPPING = "shopping"
    TWEET = "tweet"
    SPELLING = "spelling"
    VIDEO = "video"
    DISCUSSION = "discussion"
    AI_OVERVIEW = "ai_overview"
    AI_OVERVIEW_SITELINK = "ai_overview_sitelink"
    ORGANIC_SHOPPING = "organic_shopping"

class BestPositionSetEnum(StrEnum):
    TOP_3 = "top_3"
    TOP_4_10 = "top_4_10"
    TOP_11_50 = "top_11_50"
    TOP_51_MORE = "top_51_more"

class BrokenRedirectReasonEnum(StrEnum):
    DROPPEDMANUAL = "droppedmanual"
    DROPPEDTOOOLD = "droppedtooold"
    DROPPED = "dropped"
    CODECHANGED = "codechanged"
    NXDOMAIN = "nxdomain"
    ROBOTSDISALLOWED = "robotsdisallowed"
    CURLERROR = "curlerror"
    INVALIDTARGET = "invalidtarget"
    NOMORECANONICAL = "nomorecanonical"
    ISNOWPARKED = "isnowparked"
    TARGETCHANGED = "targetchanged"

class CountryEnum(StrEnum):
    AD = "ad"
    AE = "ae"
    AF = "af"
    AG = "ag"
    AI = "ai"
    AL = "al"
    AM = "am"
    AO = "ao"
    AR = "ar"
    AS = "as"
    AT = "at"
    AU = "au"
    AW = "aw"
    AZ = "az"
    BA = "ba"
    BB = "bb"
    BD = "bd"
    BE = "be"
    BF = "bf"
    BG = "bg"
    BH = "bh"
    BI = "bi"
    BJ = "bj"
    BN = "bn"
    BO = "bo"
    BR = "br"
    BS = "bs"
    BT = "bt"
    BW = "bw"
    BY = "by"
    BZ = "bz"
    CA = "ca"
    CD = "cd"
    CF = "cf"
    CG = "cg"
    CH = "ch"
    CI = "ci"
    CK = "ck"
    CL = "cl"
    CM = "cm"
    CN = "cn"
    CO = "co"
    CR = "cr"
    CU = "cu"
    CV = "cv"
    CY = "cy"
    CZ = "cz"
    DE = "de"
    DJ = "dj"
    DK = "dk"
    DM = "dm"
    DO = "do"
    DZ = "dz"
    EC = "ec"
    EE = "ee"
    EG = "eg"
    ES = "es"
    ET = "et"
    FI = "fi"
    FJ = "fj"
    FM = "fm"
    FO = "fo"
    FR = "fr"
    GA = "ga"
    GB = "gb"
    GD = "gd"
    GE = "ge"
    GF = "gf"
    GG = "gg"
    GH = "gh"
    GI = "gi"
    GL = "gl"
    GM = "gm"
    GN = "gn"
    GP = "gp"
    GQ = "gq"
    GR = "gr"
    GT = "gt"
    GU = "gu"
    GY = "gy"
    HK = "hk"
    HN = "hn"
    HR = "hr"
    HT = "ht"
    HU = "hu"
    ID = "id"
    IE = "ie"
    IL = "il"
    IM = "im"
    IN = "in"
    IQ = "iq"
    IS = "is"
    IT = "it"
    JE = "je"
    JM = "jm"
    JO = "jo"
    JP = "jp"
    KE = "ke"
    KG = "kg"
    KH = "kh"
    KI = "ki"
    KN = "kn"
    KR = "kr"
    KW = "kw"
    KY = "ky"
    KZ = "kz"
    LA = "la"
    LB = "lb"
    LC = "lc"
    LI = "li"
    LK = "lk"
    LS = "ls"
    LT = "lt"
    LU = "lu"
    LV = "lv"
    LY = "ly"
    MA = "ma"
    MC = "mc"
    MD = "md"
    ME = "me"
    MG = "mg"
    MK = "mk"
    ML = "ml"
    MM = "mm"
    MN = "mn"
    MQ = "mq"
    MR = "mr"
    MS = "ms"
    MT = "mt"
    MU = "mu"
    MV = "mv"
    MW = "mw"
    MX = "mx"
    MY = "my"
    MZ = "mz"
    NA = "na"
    NC = "nc"
    NE = "ne"
    NG = "ng"
    NI = "ni"
    NL = "nl"
    NO = "no"
    NP = "np"
    NR = "nr"
    NU = "nu"
    NZ = "nz"
    OM = "om"
    PA = "pa"
    PE = "pe"
    PF = "pf"
    PG = "pg"
    PH = "ph"
    PK = "pk"
    PL = "pl"
    PN = "pn"
    PR = "pr"
    PS = "ps"
    PT = "pt"
    PY = "py"
    QA = "qa"
    RE = "re"
    RO = "ro"
    RS = "rs"
    RU = "ru"
    RW = "rw"
    SA = "sa"
    SB = "sb"
    SC = "sc"
    SE = "se"
    SG = "sg"
    SH = "sh"
    SI = "si"
    SK = "sk"
    SL = "sl"
    SM = "sm"
    SN = "sn"
    SO = "so"
    SR = "sr"
    ST = "st"
    SV = "sv"
    TD = "td"
    TG = "tg"
    TH = "th"
    TJ = "tj"
    TK = "tk"
    TL = "tl"
    TM = "tm"
    TN = "tn"
    TO = "to"
    TR = "tr"
    TT = "tt"
    TW = "tw"
    TZ = "tz"
    UA = "ua"
    UG = "ug"
    US = "us"
    UY = "uy"
    UZ = "uz"
    VC = "vc"
    VE = "ve"
    VG = "vg"
    VI = "vi"
    VN = "vn"
    VU = "vu"
    WS = "ws"
    YE = "ye"
    YT = "yt"
    ZA = "za"
    ZM = "zm"
    ZW = "zw"

class CountryEnum1(StrEnum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    OTHER = "OTHER"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"

class DataSourceEnum(StrEnum):
    GOOGLE_AI_OVERVIEWS = "google_ai_overviews"
    GOOGLE_AI_MODE = "google_ai_mode"
    CHATGPT = "chatgpt"
    GEMINI = "gemini"
    PERPLEXITY = "perplexity"
    COPILOT = "copilot"

class DeviceEnum(StrEnum):
    DESKTOP = "desktop"
    MOBILE = "mobile"

class DiscoveredStatusEnum(StrEnum):
    PAGEFOUND = "pagefound"
    LINKFOUND = "linkfound"
    LINKRESTORED = "linkrestored"

class DropReasonEnum(StrEnum):
    MANUAL = "manual"
    NORATINGUNUSED = "noratingunused"
    NOTOP = "notop"
    TOOOLD = "tooold"
    OLDUNAVAILABLE = "oldunavailable"
    RESCURSIVE = "rescursive"
    DUPLICATE = "duplicate"
    NXDOMAIN = "nxdomain"
    MALFORMED = "malformed"
    BLOCKEDPORT = "blockedport"
    DISALLOWED = "disallowed"
    UNLINKED = "unlinked"

class FilterModeEnum(StrEnum):
    ADDED = "added"
    NEW = "new"
    REMOVED = "removed"
    MISSING = "missing"
    NO_CHANGE = "no_change"

class GroupModeEnum(StrEnum):
    DOMAINS = "domains"
    PAGES = "pages"

class HistoryGroupingEnum(StrEnum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

class LinkTypeEnum(StrEnum):
    REDIRECT = "redirect"
    FRAME = "frame"
    TEXT = "text"
    FORM = "form"
    CANONICAL = "canonical"
    ALTERNATE = "alternate"
    RSS = "rss"
    IMAGE = "image"

class LostReasonEnum(StrEnum):
    REMOVEDFROMHTML = "removedfromhtml"
    NOTCANONICAL = "notcanonical"
    NOINDEX = "noindex"
    PAGEREDIRECTED = "pageredirected"
    PAGEERROR = "pageerror"
    LOSTREDIRECT = "lostredirect"
    NOTFOUND = "notfound"

class MatchModeEnum(StrEnum):
    TERMS = "terms"
    PHRASE = "phrase"

class ModeEnum(StrEnum):
    EXACT = "exact"
    PREFIX = "prefix"
    DOMAIN = "domain"
    SUBDOMAINS = "subdomains"

class OrderByEnum(StrEnum):
    RELEVANCE = "relevance"
    VOLUME = "volume"

class OutputEnum(StrEnum):
    JSON = "json"
    CSV = "csv"
    XML = "xml"
    PHP = "php"

class OutputJsonPhpEnum(StrEnum):
    JSON = "json"
    PHP = "php"

class ProtocolEnum(StrEnum):
    BOTH = "both"
    HTTP = "http"
    HTTPS = "https"

class SearchEngineEnum(StrEnum):
    GOOGLE = "google"

class SerpFeaturesItemEnum(StrEnum):
    AI_OVERVIEW_SITELINK = "ai_overview_sitelink"
    SNIPPET = "snippet"
    AI_OVERVIEW = "ai_overview"
    LOCAL_PACK = "local_pack"
    SITELINK = "sitelink"
    NEWS = "news"
    IMAGE = "image"
    VIDEO = "video"
    DISCUSSION = "discussion"
    TWEET = "tweet"
    PAID_TOP = "paid_top"
    PAID_BOTTOM = "paid_bottom"
    PAID_SITELINK = "paid_sitelink"
    SHOPPING = "shopping"
    KNOWLEDGE_CARD = "knowledge_card"
    KNOWLEDGE_PANEL = "knowledge_panel"
    QUESTION = "question"
    IMAGE_TH = "image_th"
    VIDEO_TH = "video_th"
    ORGANIC_SHOPPING = "organic_shopping"

class SerpFeaturesItemEnum1(StrEnum):
    PAID_TOP = "paid_top"
    PAID_BOTTOM = "paid_bottom"
    PAID_RIGHT = "paid_right"
    PAID_SITELINK = "paid_sitelink"
    ORGANIC = "organic"
    SITELINK = "sitelink"
    SNIPPET = "snippet"
    IMAGE = "image"
    ARTICLE = "article"
    KNOWLEDGE_CARD = "knowledge_card"
    KNOWLEDGE_PANEL = "knowledge_panel"
    LOCAL_PACK = "local_pack"
    LOCAL_TEASER = "local_teaser"
    NEWS = "news"
    QUESTION = "question"
    REVIEW = "review"
    SHOPPING = "shopping"
    TWEET = "tweet"
    SPELLING = "spelling"
    VIDEO = "video"
    DISCUSSION = "discussion"
    AI_OVERVIEW = "ai_overview"
    AI_OVERVIEW_SITELINK = "ai_overview_sitelink"
    ORGANIC_SHOPPING = "organic_shopping"
    IMAGE_TH = "image_th"
    VIDEO_TH = "video_th"
    AI_OVERVIEW_FOUND = "ai_overview_found"

class StatusEnum(StrEnum):
    LEFT = "left"
    RIGHT = "right"
    BOTH = "both"

class TargetPositionEnum(StrEnum):
    IN_TOP10 = "in_top10"
    IN_TOP100 = "in_top100"

class TermsEnum(StrEnum):
    ALL = "all"
    QUESTIONS = "questions"

class TermsEnum1(StrEnum):
    ALSO_RANK_FOR = "also_rank_for"
    ALSO_TALK_ABOUT = "also_talk_about"
    ALL = "all"

class TldClassSourceEnum(StrEnum):
    GOV = "gov"
    EDU = "edu"
    NORMAL = "normal"

class ViewForEnum(StrEnum):
    TOP_10 = "top_10"
    TOP_100 = "top_100"

class VolumeModeEnum(StrEnum):
    MONTHLY = "monthly"
    AVERAGE = "average"

# ============== Batch Analysis API ==============

# ============== Brand Radar API ==============

# Models for brand-radar/ai-responses
class BrandRadarAiResponsesRequest(BaseModel):
    """Request model for BrandRadarAiResponsesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    date: DateStr | None = Field(default=None, description="The date to search for ...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    order_by: OrderByEnum = Field(default=OrderByEnum.RELEVANCE, description="The o...")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the ni...")
    competitors: str = Field(default="[]", description="A comma-separated list of c...")
    brand: str = Field(default="[]", description="A comma-separated list of brands ...")

class BrandRadarAiResponsesData(BaseModel):
    """Individual data item for /ai-responses endpoint"""

    country: str | None = Field(default=None, description="The country of the quest...")
    links: list[dict[str, Any] | None] | None = Field(default=None, description="(1...")
    question: str | None = Field(default=None, description="The question asked by t...")
    response: str | None = Field(default=None, description="(10 units) The response...")
    volume: int | None = Field(default=None, description="(10 units) Estimated mont...")

class BrandRadarAiResponsesResponse(BaseModel):
    """Response model for /ai-responses endpoint"""

    ai_responses: list[BrandRadarAiResponsesData] | None = Field(default=None)

    @property
    def data(self) -> list[BrandRadarAiResponsesData]:
        """Unwrap the response payload."""
        return self.ai_responses or []


# Models for brand-radar/impressions-history
class BrandRadarImpressionsHistoryRequest(BaseModel):
    """Request model for BrandRadarImpressionsHistoryRequest."""

    where: str | None = Field(default=None, description="The filter expression. The...")
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the ni...")
    brand: str = Field(..., description="The brand to search for.")

class BrandRadarImpressionsHistoryData(BaseModel):
    """Individual data item for /impressions-history endpoint"""

    date: str | None = Field(default=None, description="date")
    impressions: int | None = Field(default=None, description="impressions")

class BrandRadarImpressionsHistoryResponse(BaseModel):
    """Response model for /impressions-history endpoint"""

    metrics: list[BrandRadarImpressionsHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[BrandRadarImpressionsHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/impressions-overview
class BrandRadarImpressionsOverviewRequest(BaseModel):
    """Request model for BrandRadarImpressionsOverviewRequest."""

    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the ni...")
    competitors: str = Field(default="[]", description="A comma-separated list of c...")
    brand: str = Field(default="[]", description="A comma-separated list of brands ...")

class BrandRadarImpressionsOverviewData(BaseModel):
    """Individual data item for /impressions-overview endpoint"""

    brand: str | None = Field(default=None, description="Brand name (either your br...")
    no_tracked_brands: int | None = Field(default=None, description="Estimated impr...")
    only_competitors_brands: int | None = Field(default=None, description="Estimate...")
    only_target_brand: int | None = Field(default=None, description="Estimated impr...")
    target_and_competitors_brands: int | None = Field(default=None, description="Es...")
    total: int | None = Field(default=None, description="Total estimated impression...")

class BrandRadarImpressionsOverviewResponse(BaseModel):
    """Response model for /impressions-overview endpoint"""

    metrics: list[BrandRadarImpressionsOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[BrandRadarImpressionsOverviewData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/mentions-history
class BrandRadarMentionsHistoryRequest(BaseModel):
    """Request model for BrandRadarMentionsHistoryRequest."""

    where: str | None = Field(default=None, description="The filter expression. The...")
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the ni...")
    brand: str = Field(..., description="The brand to search for.")

class BrandRadarMentionsHistoryData(BaseModel):
    """Individual data item for /mentions-history endpoint"""

    date: str | None = Field(default=None, description="date")
    mentions: int | None = Field(default=None, description="mentions")

class BrandRadarMentionsHistoryResponse(BaseModel):
    """Response model for /mentions-history endpoint"""

    metrics: list[BrandRadarMentionsHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[BrandRadarMentionsHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/mentions-overview
class BrandRadarMentionsOverviewRequest(BaseModel):
    """Request model for BrandRadarMentionsOverviewRequest."""

    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the ni...")
    competitors: str = Field(default="[]", description="A comma-separated list of c...")
    brand: str = Field(default="[]", description="A comma-separated list of brands ...")

class BrandRadarMentionsOverviewData(BaseModel):
    """Individual data item for /mentions-overview endpoint"""

    brand: str | None = Field(default=None, description="Brand name (either your br...")
    no_tracked_brands: int | None = Field(default=None, description="Estimated ment...")
    only_competitors_brands: int | None = Field(default=None, description="Estimate...")
    only_target_brand: int | None = Field(default=None, description="Estimated ment...")
    target_and_competitors_brands: int | None = Field(default=None, description="Es...")
    total: int | None = Field(default=None, description="Total estimated mentions f...")

class BrandRadarMentionsOverviewResponse(BaseModel):
    """Response model for /mentions-overview endpoint"""

    metrics: list[BrandRadarMentionsOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[BrandRadarMentionsOverviewData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/sov-overview
class BrandRadarSovOverviewRequest(BaseModel):
    """Request model for BrandRadarSovOverviewRequest."""

    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the ni...")
    competitors: str = Field(default="[]", description="A comma-separated list of c...")
    brand: str = Field(default="[]", description="A comma-separated list of brands ...")

class BrandRadarSovOverviewData(BaseModel):
    """Individual data item for /sov-overview endpoint"""

    brand: str | None = Field(default=None, description="Brand name (either your br...")
    share_of_voice: float | None = Field(default=None, description="Estimated share...")

class BrandRadarSovOverviewResponse(BaseModel):
    """Response model for /sov-overview endpoint"""

    metrics: list[BrandRadarSovOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[BrandRadarSovOverviewData]:
        """Unwrap the response payload."""
        return self.metrics or []


# ============== Keywords Explorer API ==============

# Models for keywords-explorer/matching-terms
class KeywordsExplorerMatchingTermsRequest(BaseModel):
    """Request model for KeywordsExplorerMatchingTermsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE)
    keywords: str | None = Field(default=None, description="A comma-separated list ...")
    keyword_list_id: int | None = Field(default=None, description="The id of an exi...")
    match_mode: MatchModeEnum = Field(default=MatchModeEnum.TERMS, description="Key...")
    terms: TermsEnum = Field(default=TermsEnum.ALL, description="All keywords ideas...")

class KeywordsExplorerMatchingTermsData(BaseModel):
    """Individual data item for /matching-terms endpoint"""

    cpc: int | None = Field(default=None, description="Cost Per Click shows the ave...")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS)...")
    difficulty: int | None = Field(default=None, description="(10 units) An estimat...")
    first_seen: str | None = Field(default=None, description="The date when we firs...")
    global_volume: int | None = Field(default=None, description="(10 units) How man...")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) In...")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determ...")
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None)
    serp_last_update: str | None = Field(default=None, description="The date when w...")
    traffic_potential: int | None = Field(default=None, description="(10 units) The...")
    volume: int | None = Field(default=None, description="(10 units) An estimation ...")
    volume_desktop_pct: float | None = Field(default=None, description="The percent...")
    volume_mobile_pct: float | None = Field(default=None, description="The percenta...")
    volume_monthly: int | None = Field(default=None, description="(10 units) An est...")

class KeywordsExplorerMatchingTermsResponse(BaseModel):
    """Response model for /matching-terms endpoint"""

    keywords: list[KeywordsExplorerMatchingTermsData] | None = Field(default=None)

    @property
    def data(self) -> list[KeywordsExplorerMatchingTermsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/overview
class KeywordsExplorerOverviewRequest(BaseModel):
    """Request model for KeywordsExplorerOverviewRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    volume_monthly_date_to: DateStr | None = Field(default=None, description="The e...")
    volume_monthly_date_from: DateStr | None = Field(default=None, description="The...")
    target_mode: ModeEnum | None = Field(default=None, description="The scope of th...")
    target: str | None = Field(default=None, description="The target of the search:...")
    target_position: TargetPositionEnum | None = Field(default=None, description="F...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE)
    keywords: str | None = Field(default=None, description="A comma-separated list ...")
    keyword_list_id: int | None = Field(default=None, description="The id of an exi...")

class KeywordsExplorerOverviewData(BaseModel):
    """Individual data item for /overview endpoint"""

    clicks: int | None = Field(default=None, description="The average monthly numbe...")
    cpc: int | None = Field(default=None, description="Cost Per Click shows the ave...")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS)...")
    difficulty: int | None = Field(default=None, description="(10 units) An estimat...")
    first_seen: str | None = Field(default=None, description="The date when we firs...")
    global_volume: int | None = Field(default=None, description="(10 units) How man...")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) In...")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determ...")
    parent_volume: int | None = Field(default=None, description="(10 units) The sea...")
    searches_pct_clicks_organic_and_paid: float | None = Field(default=None)
    searches_pct_clicks_organic_only: float | None = Field(default=None)
    searches_pct_clicks_paid_only: float | None = Field(default=None)
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None)
    serp_last_update: str | None = Field(default=None, description="The date when w...")
    traffic_potential: int | None = Field(default=None, description="(10 units) The...")
    volume: int | None = Field(default=None, description="(10 units) An estimation ...")
    volume_desktop_pct: float | None = Field(default=None, description="The percent...")
    volume_mobile_pct: float | None = Field(default=None, description="The percenta...")
    volume_monthly: int | None = Field(default=None, description="(10 units) An est...")
    volume_monthly_history: list[dict[str, Any] | None] | None = Field(default=None)

class KeywordsExplorerOverviewResponse(BaseModel):
    """Response model for /overview endpoint"""

    keywords: list[KeywordsExplorerOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[KeywordsExplorerOverviewData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/related-terms
class KeywordsExplorerRelatedTermsRequest(BaseModel):
    """Request model for KeywordsExplorerRelatedTermsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    keywords: str | None = Field(default=None, description="A comma-separated list ...")
    keyword_list_id: int | None = Field(default=None, description="The id of an exi...")
    view_for: ViewForEnum = Field(default=ViewForEnum.TOP_10, description="View key...")
    terms: TermsEnum1 = Field(default=TermsEnum1.ALL, description="Related keywords...")

class KeywordsExplorerRelatedTermsData(BaseModel):
    """Individual data item for /related-terms endpoint"""

    cpc: int | None = Field(default=None, description="Cost Per Click shows the ave...")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS)...")
    difficulty: int | None = Field(default=None, description="(10 units) An estimat...")
    first_seen: str | None = Field(default=None, description="The date when we firs...")
    global_volume: int | None = Field(default=None, description="(10 units) How man...")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) In...")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determ...")
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None)
    serp_last_update: str | None = Field(default=None, description="The date when w...")
    traffic_potential: int | None = Field(default=None, description="(10 units) The...")
    volume: int | None = Field(default=None, description="(10 units) An estimation ...")
    volume_desktop_pct: float | None = Field(default=None, description="The percent...")
    volume_mobile_pct: float | None = Field(default=None, description="The percenta...")
    volume_monthly: int | None = Field(default=None, description="(10 units) An est...")

class KeywordsExplorerRelatedTermsResponse(BaseModel):
    """Response model for /related-terms endpoint"""

    keywords: list[KeywordsExplorerRelatedTermsData] | None = Field(default=None)

    @property
    def data(self) -> list[KeywordsExplorerRelatedTermsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/search-suggestions
class KeywordsExplorerSearchSuggestionsRequest(BaseModel):
    """Request model for KeywordsExplorerSearchSuggestionsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE)
    keywords: str | None = Field(default=None, description="A comma-separated list ...")
    keyword_list_id: int | None = Field(default=None, description="The id of an exi...")

class KeywordsExplorerSearchSuggestionsData(BaseModel):
    """Individual data item for /search-suggestions endpoint"""

    cpc: int | None = Field(default=None, description="Cost Per Click shows the ave...")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS)...")
    difficulty: int | None = Field(default=None, description="(10 units) An estimat...")
    first_seen: str | None = Field(default=None, description="The date when we firs...")
    global_volume: int | None = Field(default=None, description="(10 units) How man...")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) In...")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determ...")
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None)
    serp_last_update: str | None = Field(default=None, description="The date when w...")
    traffic_potential: int | None = Field(default=None, description="(10 units) The...")
    volume: int | None = Field(default=None, description="(10 units) An estimation ...")
    volume_desktop_pct: float | None = Field(default=None, description="The percent...")
    volume_mobile_pct: float | None = Field(default=None, description="The percenta...")
    volume_monthly: int | None = Field(default=None, description="(10 units) An est...")

class KeywordsExplorerSearchSuggestionsResponse(BaseModel):
    """Response model for /search-suggestions endpoint"""

    keywords: list[KeywordsExplorerSearchSuggestionsData] | None = Field(default=None)

    @property
    def data(self) -> list[KeywordsExplorerSearchSuggestionsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/volume-by-country
class KeywordsExplorerVolumeByCountryRequest(BaseModel):
    """Request model for KeywordsExplorerVolumeByCountryRequest."""

    limit: int | None = Field(default=None, description="The number of results to r...")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE)
    keyword: str = Field(..., description="The keyword to show metrics for.")

class KeywordsExplorerVolumeByCountryData(BaseModel):
    """Individual data item for /volume-by-country endpoint"""

    country: str | None = Field(default=None, description="The country field")
    volume: int | None = Field(default=None, description="(10 units) An estimation ...")

class KeywordsExplorerVolumeByCountryResponse(BaseModel):
    """Response model for /volume-by-country endpoint"""

    countries: list[KeywordsExplorerVolumeByCountryData] | None = Field(default=None)

    @property
    def data(self) -> list[KeywordsExplorerVolumeByCountryData]:
        """Unwrap the response payload."""
        return self.countries or []


# Models for keywords-explorer/volume-history
class KeywordsExplorerVolumeHistoryRequest(BaseModel):
    """Request model for KeywordsExplorerVolumeHistoryRequest."""

    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr | None = Field(default=None, description="The start date of ...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    keyword: str = Field(..., description="The keyword to show metrics for.")

class KeywordsExplorerVolumeHistoryData(BaseModel):
    """Individual data item for /volume-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    volume: int | None = Field(default=None, description="An estimation of the numb...")

class KeywordsExplorerVolumeHistoryResponse(BaseModel):
    """Response model for /volume-history endpoint"""

    metrics: list[KeywordsExplorerVolumeHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[KeywordsExplorerVolumeHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# ============== Rank Tracker API ==============

# Models for rank-tracker/competitors-overview
class RankTrackerCompetitorsOverviewRequest(BaseModel):
    """Request model for RankTrackerCompetitorsOverviewRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    date_compared: DateStr | None = Field(default=None, description="A date to comp...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop ...")
    project_id: int = Field(..., description="The unique identifier of the project....")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class RankTrackerCompetitorsOverviewData(BaseModel):
    """Individual data item for /competitors-overview endpoint"""

    competitors_list: list[dict[str, Any] | None] | None = Field(default=None)
    country: CountryEnum1 | None = Field(default=None, description="The country tha...")
    keyword: str | None = Field(default=None, description="The keyword your target ...")
    keyword_difficulty: int | None = Field(default=None, description="An estimation...")
    keyword_has_data: bool | None = Field(default=None, description="Will return `f...")
    keyword_is_frozen: bool | None = Field(default=None, description="Indicates whe...")
    language: str | None = Field(default=None, description="The SERP language that ...")
    location: str | None = Field(default=None, description="The location (country, ...")
    serp_features: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None)
    serp_updated: str | None = Field(default=None, description="The date when we la...")
    serp_updated_prev: str | None = Field(default=None, description="The date when ...")
    tags: list[str | None] | None = Field(default=None, description="A list of tags...")
    volume: int | None = Field(default=None, description="An estimation of the aver...")

class RankTrackerCompetitorsOverviewResponse(BaseModel):
    """Response model for /competitors-overview endpoint"""

    keywords: list[RankTrackerCompetitorsOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[RankTrackerCompetitorsOverviewData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for rank-tracker/competitors-pages
class RankTrackerCompetitorsPagesRequest(BaseModel):
    """Request model for RankTrackerCompetitorsPagesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    target_and_tracked_competitors_only: bool = Field(default=False, description="R...")
    date_compared: DateStr | None = Field(default=None, description="A date to comp...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop ...")
    project_id: int = Field(..., description="The unique identifier of the project....")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class RankTrackerCompetitorsPagesData(BaseModel):
    """Individual data item for /competitors-pages endpoint"""

    keywords: int | None = Field(default=None, description="The total number of key...")
    share_of_traffic_value: float | None = Field(default=None, description="The sha...")
    share_of_traffic_value_prev: float | None = Field(default=None, description="Th...")
    share_of_voice: float | None = Field(default=None, description="The share of yo...")
    share_of_voice_prev: float | None = Field(default=None, description="The share ...")
    status: StatusEnum | None = Field(default=None, description="The status of a pa...")
    title: str | None = Field(default=None, description="The title displayed for th...")
    title_prev: str | None = Field(default=None, description="The title on the comp...")
    traffic: int | None = Field(default=None, description="An estimation of the num...")
    traffic_prev: int | None = Field(default=None, description="The traffic on the ...")
    traffic_value: int | None = Field(default=None, description="The estimated valu...")
    traffic_value_prev: int | None = Field(default=None, description="The traffic v...")
    url: str | None = Field(default=None, description="The page URL.")

class RankTrackerCompetitorsPagesResponse(BaseModel):
    """Response model for /competitors-pages endpoint"""

    competitors_pages: list[RankTrackerCompetitorsPagesData] | None = Field(default=None, alias="competitors-pages")

    @property
    def data(self) -> list[RankTrackerCompetitorsPagesData]:
        """Unwrap the response payload."""
        return self.competitors_pages or []


# Models for rank-tracker/competitors-stats
class RankTrackerCompetitorsStatsRequest(BaseModel):
    """Request model for RankTrackerCompetitorsStatsRequest."""

    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop ...")
    project_id: int = Field(..., description="The unique identifier of the project....")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class RankTrackerCompetitorsStatsData(BaseModel):
    """Individual data item for /competitors-stats endpoint"""

    ai_overview_count: int | None = Field(default=None, description="The total numb...")
    average_position: float | None = Field(default=None, description="The average o...")
    competitor: str | None = Field(default=None, description="Competitor's URL.")
    discussions_count: int | None = Field(default=None, description="The total numb...")
    featured_snippet_count: int | None = Field(default=None, description="The total...")
    image_pack_count: int | None = Field(default=None, description="The total numbe...")
    knowledge_card_count: int | None = Field(default=None, description="The total n...")
    knowledge_panel_count: int | None = Field(default=None, description="The total ...")
    pos_11_20: int | None = Field(default=None, description="The total number of tr...")
    pos_1_3: int | None = Field(default=None, description="The total number of trac...")
    pos_21_50: int | None = Field(default=None, description="The total number of tr...")
    pos_4_10: int | None = Field(default=None, description="The total number of tra...")
    pos_51_plus: int | None = Field(default=None, description="The total number of ...")
    pos_no_rank: int | None = Field(default=None, description="The total number of ...")
    share_of_traffic_value: float | None = Field(default=None, description="The sha...")
    share_of_voice: float | None = Field(default=None, description="The share of yo...")
    sitelinks_count: int | None = Field(default=None, description="The total number...")
    thumbnail_count: int | None = Field(default=None, description="The total number...")
    top_stories_count: int | None = Field(default=None, description="The total numb...")
    traffic: int | None = Field(default=None, description="The estimated number of ...")
    traffic_value: int | None = Field(default=None, description="The estimated valu...")
    video_preview_count: int | None = Field(default=None, description="The total nu...")
    videos_count: int | None = Field(default=None, description="The total number of...")
    x_count: int | None = Field(default=None, description="The total number of trac...")

class RankTrackerCompetitorsStatsResponse(BaseModel):
    """Response model for /competitors-stats endpoint"""

    competitors_metrics: list[RankTrackerCompetitorsStatsData] | None = Field(default=None, alias="competitors-metrics")

    @property
    def data(self) -> list[RankTrackerCompetitorsStatsData]:
        """Unwrap the response payload."""
        return self.competitors_metrics or []


# Models for rank-tracker/overview
class RankTrackerOverviewRequest(BaseModel):
    """Request model for RankTrackerOverviewRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    date_compared: DateStr | None = Field(default=None, description="A date to comp...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop ...")
    project_id: int = Field(..., description="The unique identifier of the project....")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class RankTrackerOverviewData(BaseModel):
    """Individual data item for /overview endpoint"""

    best_position_has_thumbnail: bool | None = Field(default=None, description="The...")
    best_position_has_thumbnail_previous: bool | None = Field(default=None)
    best_position_has_video_preview: bool | None = Field(default=None)
    best_position_has_video_preview_previous: bool | None = Field(default=None)
    best_position_kind: BestPositionKindEnum | None = Field(default=None)
    best_position_kind_previous: BestPositionKindEnum | None = Field(default=None)
    clicks: int | None = Field(default=None, description="Clicks metric refers to t...")
    clicks_per_search: float | None = Field(default=None, description="Clicks Per S...")
    cost_per_click: int | None = Field(default=None, description="Cost Per Click sh...")
    country: CountryEnum1 | None = Field(default=None, description="The country tha...")
    country_prev: CountryEnum1 | None = Field(default=None, description="The countr...")
    created_at: str | None = Field(default=None, description="The date when a keywo...")
    is_branded: bool | None = Field(default=None, description="User intent: branded...")
    is_commercial: bool | None = Field(default=None, description="User intent: comm...")
    is_informational: bool | None = Field(default=None, description="User intent: i...")
    is_local: bool | None = Field(default=None, description="User intent: local. Th...")
    is_navigational: bool | None = Field(default=None, description="User intent: na...")
    is_transactional: bool | None = Field(default=None, description="User intent: t...")
    keyword: str | None = Field(default=None, description="The keyword your target ...")
    keyword_difficulty: int | None = Field(default=None, description="An estimation...")
    keyword_has_data: bool | None = Field(default=None, description="Will return `f...")
    keyword_is_frozen: bool | None = Field(default=None, description="Indicates whe...")
    keyword_prev: str | None = Field(default=None, description="The keyword your ta...")
    language: str | None = Field(default=None, description="The SERP language that ...")
    language_prev: str | None = Field(default=None, description="The SERP language ...")
    location: str | None = Field(default=None, description="The location (country, ...")
    location_prev: str | None = Field(default=None, description="The location (coun...")
    parent_topic: str | None = Field(default=None, description="Parent Topic determ...")
    position: int | None = Field(default=None, description="The top position (or ta...")
    position_diff: int | None = Field(default=None, description="The change in top ...")
    position_prev: int | None = Field(default=None, description="The top position (...")
    search_type_image: float | None = Field(default=None, description="Search type ...")
    search_type_news: float | None = Field(default=None, description="Search type N...")
    search_type_video: float | None = Field(default=None, description="Search type ...")
    search_type_web: float | None = Field(default=None, description="Search type We...")
    serp_features: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None)
    serp_features_prev: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None)
    serp_updated: str | None = Field(default=None, description="The date when we la...")
    serp_updated_prev: str | None = Field(default=None, description="The date when ...")
    tags: list[str | None] | None = Field(default=None, description="A list of tags...")
    tags_prev: list[str | None] | None = Field(default=None, description="A list of...")
    target_positions_count: int | None = Field(default=None, description="The numbe...")
    traffic: int | None = Field(default=None, description="An estimation of the num...")
    traffic_diff: int | None = Field(default=None, description="The change in traff...")
    traffic_prev: int | None = Field(default=None, description="An estimation of th...")
    url: str | None = Field(default=None, description="The top-ranking URL (or targ...")
    url_prev: str | None = Field(default=None, description="The top-ranking URL (or...")
    volume: int | None = Field(default=None, description="An estimation of the aver...")
    volume_desktop_pct: float | None = Field(default=None, description="The percent...")
    volume_mobile_pct: float | None = Field(default=None, description="The percenta...")

class RankTrackerOverviewResponse(BaseModel):
    """Response model for /overview endpoint"""

    overviews: list[RankTrackerOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[RankTrackerOverviewData]:
        """Unwrap the response payload."""
        return self.overviews or []


# Models for rank-tracker/serp-overview
class RankTrackerSerpOverviewRequest(BaseModel):
    """Request model for RankTrackerSerpOverviewRequest."""

    top_positions: int | None = Field(default=None, description="The number of top ...")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop ...")
    date: str | None = Field(default=None, description="A timestamp on which the la...")
    location_id: int | None = Field(default=None, description="The location ID of a...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    language_code: str | None = Field(default=None, description="The language code ...")
    keyword: str = Field(..., description="The keyword to return SERP Overview for.")
    project_id: int = Field(..., description="The unique identifier of the project....")

class RankTrackerSerpOverviewData(BaseModel):
    """Individual data item for /serp-overview endpoint"""

    position: int | None = Field(default=None, description="The position of the sea...")
    title: str | None = Field(default=None, description="The title of a ranking page.")
    url: str | None = Field(default=None, description="The URL of a ranking page.")
    type: list[str | None] | None = Field(default=None, description="The kind of th...")
    update_date: str | None = Field(default=None, description="The date when we che...")
    nr_words: int | None = Field(default=None, description="The total number of wor...")
    domain_rating: float | None = Field(default=None, description="The strength of ...")
    url_rating: float | None = Field(default=None, description="The strength of a p...")
    ahrefs_rank: int | None = Field(default=None, description="The strength of a do...")
    backlinks: int | None = Field(default=None, description="The total number of li...")
    refdomains: int | None = Field(default=None, description="The total number of u...")
    traffic: int | None = Field(default=None, description="An estimation of the mon...")
    value: int | None = Field(default=None, description="The estimated value of a p...")
    keywords: int | None = Field(default=None, description="The total number of key...")
    top_keyword: str | None = Field(default=None, description="The keyword that bri...")
    top_keyword_volume: int | None = Field(default=None, description="An estimation...")

class RankTrackerSerpOverviewResponse(BaseModel):
    """Response model for /serp-overview endpoint"""

    positions: list[RankTrackerSerpOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[RankTrackerSerpOverviewData]:
        """Unwrap the response payload."""
        return self.positions or []


# ============== Serp Overview API ==============

# Models for serp-overview/serp-overview
class SerpOverviewSerpOverviewRequest(BaseModel):
    """Request model for SerpOverviewSerpOverviewRequest."""

    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    top_positions: int | None = Field(default=None, description="The number of top ...")
    date: str | None = Field(default=None, description="A timestamp on which the la...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    keyword: str = Field(..., description="The keyword to return SERP Overview for.")

class SerpOverviewSerpOverviewData(BaseModel):
    """Individual data item for /serp-overview endpoint"""

    ahrefs_rank: int | None = Field(default=None, description="The strength of a do...")
    backlinks: int | None = Field(default=None, description="The total number of li...")
    domain_rating: float | None = Field(default=None, description="The strength of ...")
    keywords: int | None = Field(default=None, description="The total number of key...")
    position: int | None = Field(default=None, description="The position of the sea...")
    refdomains: int | None = Field(default=None, description="(5 units) The total n...")
    title: str | None = Field(default=None, description="The title of a ranking page.")
    top_keyword: str | None = Field(default=None, description="The keyword that bri...")
    top_keyword_volume: int | None = Field(default=None, description="(10 units) An...")
    traffic: int | None = Field(default=None, description="(10 units) An estimation...")
    type: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None)
    update_date: str | None = Field(default=None, description="The date when we che...")
    url: str | None = Field(default=None, description="The URL of a ranking page.")
    url_rating: float | None = Field(default=None, description="The strength of a p...")
    value: int | None = Field(default=None, description="(10 units) The estimated v...")

class SerpOverviewSerpOverviewResponse(BaseModel):
    """Response model for /serp-overview endpoint"""

    positions: list[SerpOverviewSerpOverviewData] | None = Field(default=None)

    @property
    def data(self) -> list[SerpOverviewSerpOverviewData]:
        """Unwrap the response payload."""
        return self.positions or []


# ============== Site Audit API ==============

# Models for site-audit/issues
class SiteAuditIssuesRequest(BaseModel):
    """Request model for SiteAuditIssuesRequest."""

    date_compared: str | None = Field(default=None, description="A timestamp in `YY...")
    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDT...")
    project_id: int = Field(..., description="The unique identifier of the project....")

class SiteAuditIssuesData(BaseModel):
    """Individual data item for /issues endpoint"""

    issue_id: str | None = Field(default=None, description="The unique identifier o...")
    name: str | None = Field(default=None, description="The name of the issue.")
    importance: str | None = Field(default=None, description="The importance of the...")
    category: str | None = Field(default=None, description="The category of the iss...")
    is_indexable: bool | None = Field(default=None, description="True if the issue ...")
    crawled: int | None = Field(default=None, description="Number of URLs currently...")
    change: int | None = Field(default=None, description="Difference in the number ...")
    added: int | None = Field(default=None, description="Number of URLs that have t...")
    new: int | None = Field(default=None, description="Number of newly discovered U...")
    removed: int | None = Field(default=None, description="Number of URLs that had ...")
    missing: int | None = Field(default=None, description="Number of URLs that had ...")

class SiteAuditIssuesResponse(BaseModel):
    """Response model for /issues endpoint"""

    issues: list[SiteAuditIssuesData] | None = Field(default=None, description="The...")

    @property
    def data(self) -> list[SiteAuditIssuesData]:
        """Unwrap the response payload."""
        return self.issues or []


# Models for site-audit/page-content
class SiteAuditPageContentRequest(BaseModel):
    """Request model for SiteAuditPageContentRequest."""

    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDT...")
    target_url: str = Field(..., description="The URL of the page to retrieve conte...")
    project_id: int = Field(..., description="The unique identifier of the project....")

class SiteAuditPageContentData(BaseModel):
    """Individual data item for /page-content endpoint"""

    crawl_datetime: str | None = Field(default=None, description="The timestamp whe...")
    page_text: str | None = Field(default=None, description="The text extracted fro...")
    raw_html: str | None = Field(default=None, description="The raw HTML of the page.")
    rendered_html: str | None = Field(default=None, description="The rendered HTML ...")

class SiteAuditPageContentResponse(BaseModel):
    """Response model for /page-content endpoint"""

    page_content: SiteAuditPageContentData | None = Field(default=None, alias="page-content")

    @property
    def data(self) -> SiteAuditPageContentData | None:
        """Unwrap the response payload."""
        return self.page_content


# Models for site-audit/page-explorer
class SiteAuditPageExplorerRequest(BaseModel):
    """Request model for SiteAuditPageExplorerRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(default="page_rating,url,is_rendered,http_code,content_type,title,meta_description,h1,traffic,canonical,canonical_code,redirect,redirect_code,compliant,page_is_noindex,page_is_nofollow,incoming_all_links,links_count_internal,links_count_external,links_count_internal4xx,links_count_external4xx,hreflang_issues,psi_crux_cls_category,psi_crux_lcp_category,psi_crux_inp_category,jsonld_schema_types,jsonld_validation_kinds,origin,depth")
    filter_mode: FilterModeEnum | None = Field(default=None, description="Indicates...")
    issue_id: str | None = Field(default=None, description="The unique identifier o...")
    date_compared: str | None = Field(default=None, description="A timestamp in `YY...")
    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDT...")
    project_id: int = Field(..., description="The unique identifier of the project....")

class SiteAuditPageExplorerData(BaseModel):
    """Individual data item for /page-explorer endpoint"""

    ai_content_level: str | None = Field(default=None, description="The estimated p...")
    ai_content_status: str | None = Field(default=None, description="AI detection s...")
    alternate: int | None = Field(default=None, description="The number of incoming...")
    alternate_diff: int | None = Field(default=None, description="The number of inc...")
    alternate_prev: int | None = Field(default=None, description="The number of inc...")
    backlinks: int | None = Field(default=None, description="The number of incoming...")
    backlinks_diff: int | None = Field(default=None, description="The number of inc...")
    backlinks_prev: int | None = Field(default=None, description="The number of inc...")
    canonical: str | None = Field(default=None, description="The URL of the canonic...")
    canonical_code: int | None = Field(default=None, description="The HTTP status c...")
    canonical_counts: int | None = Field(default=None, description="The number of i...")
    canonical_counts_diff: int | None = Field(default=None, description="The number...")
    canonical_counts_prev: int | None = Field(default=None, description="The number...")
    canonical_group_hash: int | None = Field(default=None, description="The ID of t...")
    canonical_is_canonical: bool | None = Field(default=None, description="Indicate...")
    canonical_is_canonical_prev: bool | None = Field(default=None, description="Ind...")
    canonical_no_crawl_reason: str | None = Field(default=None, description="The re...")
    canonical_no_crawl_reason_prev: str | None = Field(default=None, description="T...")
    canonical_prev: str | None = Field(default=None, description="The URL of the ca...")
    canonical_scheme: str | None = Field(default=None, description="The protocol of...")
    canonical_scheme_prev: str | None = Field(default=None, description="The protoc...")
    compliant: bool | None = Field(default=None, description="Indicates that the pa...")
    compliant_prev: bool | None = Field(default=None, description="Indicates that t...")
    compression: str | None = Field(default=None, description="The data compression...")
    compression_prev: str | None = Field(default=None, description="The data compre...")
    content_encoding: str | None = Field(default=None, description="The Content-Enc...")
    content_encoding_prev: str | None = Field(default=None, description="The Conten...")
    content_length: int | None = Field(default=None, description="The character len...")
    content_length_diff: int | None = Field(default=None, description="The characte...")
    content_length_prev: int | None = Field(default=None, description="The characte...")
    content_nr_word: int | None = Field(default=None, description="The word count o...")
    content_nr_word_diff: int | None = Field(default=None, description="The word co...")
    content_nr_word_prev: int | None = Field(default=None, description="The word co...")
    content_type: str | None = Field(default=None, description="The Content-Type HT...")
    content_type_prev: str | None = Field(default=None, description="The Content-Ty...")
    css_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None)
    css_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None)
    curl_code: int | None = Field(default=None, description="CURLcode return code. ...")
    depth: int | None = Field(default=None, description="The minimum number of clic...")
    depth_diff: int | None = Field(default=None, description="The minimum number of...")
    depth_prev: int | None = Field(default=None, description="The minimum number of...")
    dofollow: int | None = Field(default=None, description="The number of incoming ...")
    dofollow_prev: int | None = Field(default=None, description="The number of inco...")
    domain: str | None = Field(default=None, description="The domain name part of t...")
    duplicate_content: int | None = Field(default=None, description="The number of ...")
    duplicate_content_canonical_hreflang: int | None = Field(default=None)
    duplicate_content_canonical_hreflang_diff: int | None = Field(default=None)
    duplicate_content_canonical_hreflang_prev: int | None = Field(default=None)
    duplicate_content_diff: int | None = Field(default=None, description="The numbe...")
    duplicate_content_prev: int | None = Field(default=None, description="The numbe...")
    duplicate_description: int | None = Field(default=None, description="The number...")
    duplicate_description_canonical_hreflang: int | None = Field(default=None)
    duplicate_description_canonical_hreflang_diff: int | None = Field(default=None)
    duplicate_description_canonical_hreflang_prev: int | None = Field(default=None)
    duplicate_description_diff: int | None = Field(default=None, description="The n...")
    duplicate_description_prev: int | None = Field(default=None, description="The n...")
    duplicate_group_identifier: int | None = Field(default=None, description="The I...")
    duplicate_h1: int | None = Field(default=None, description="The number of pages...")
    duplicate_h1_diff: int | None = Field(default=None, description="The number of ...")
    duplicate_h1_prev: int | None = Field(default=None, description="The number of ...")
    duplicate_h1canonical_hreflang: int | None = Field(default=None, description="T...")
    duplicate_h1canonical_hreflang_diff: int | None = Field(default=None)
    duplicate_h1canonical_hreflang_prev: int | None = Field(default=None)
    duplicate_title: int | None = Field(default=None, description="The number of pa...")
    duplicate_title_canonical_hreflang: int | None = Field(default=None)
    duplicate_title_canonical_hreflang_diff: int | None = Field(default=None)
    duplicate_title_canonical_hreflang_prev: int | None = Field(default=None)
    duplicate_title_diff: int | None = Field(default=None, description="The number ...")
    duplicate_title_prev: int | None = Field(default=None, description="The number ...")
    edu: int | None = Field(default=None, description="The number of incoming exter...")
    edu_diff: int | None = Field(default=None, description="The number of incoming ...")
    edu_prev: int | None = Field(default=None, description="The number of incoming ...")
    external_code: list[dict[str, Any] | None] | None = Field(default=None)
    external_link_anchor: list[dict[str, Any] | None] | None = Field(default=None)
    external_link_anchor_prev: list[dict[str, Any] | None] | None = Field(default=None)
    external_link_domain: list[str | None] | None = Field(default=None)
    external_link_domain_prev: list[str | None] | None = Field(default=None)
    external_links: list[str | None] | None = Field(default=None, description="The ...")
    external_links_is_canonical: list[dict[str, Any] | None] | None = Field(default=None)
    external_links_is_canonical_prev: list[dict[str, Any] | None] | None = Field(default=None)
    external_links_prev: list[str | None] | None = Field(default=None)
    external_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None)
    external_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None)
    external_scheme: list[str | None] | None = Field(default=None, description="The...")
    external_scheme_prev: list[str | None] | None = Field(default=None)
    final_redirect: str | None = Field(default=None, description="The destination o...")
    final_redirect_code: int | None = Field(default=None, description="The HTTP sta...")
    final_redirect_no_crawl_reason: str | None = Field(default=None, description="T...")
    final_redirect_no_crawl_reason_prev: str | None = Field(default=None)
    final_redirect_prev: str | None = Field(default=None, description="The destinat...")
    found_in_sitemaps: list[str | None] | None = Field(default=None, description="T...")
    found_in_sitemaps_length: int | None = Field(default=None, description="The num...")
    found_in_sitemaps_prev: list[str | None] | None = Field(default=None)
    gov: int | None = Field(default=None, description="The total number of incoming...")
    gov_diff: int | None = Field(default=None, description="The total number of inc...")
    gov_prev: int | None = Field(default=None, description="The total number of inc...")
    h1: list[str | None] | None = Field(default=None, description="The page H1 subh...")
    h1_prev: list[str | None] | None = Field(default=None, description="The page H1...")
    h1length: list[int | None] | None = Field(default=None, description="The charac...")
    h1length_prev: list[int | None] | None = Field(default=None, description="The c...")
    h2: list[str | None] | None = Field(default=None, description="The page H2 subh...")
    h2_prev: list[str | None] | None = Field(default=None, description="The page H2...")
    hash_content: int | None = Field(default=None, description="The page content fi...")
    hash_descriptions: list[int | None] | None = Field(default=None, description="m...")
    hash_h1: list[int | None] | None = Field(default=None, description="The page H1...")
    hash_text: int | None = Field(default=None, description="The page text fingerpr...")
    hash_titles: list[int | None] | None = Field(default=None, description="The pag...")
    hreflang: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_code_is_valid: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_code_is_valid_prev: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_country: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_country_prev: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_group_hash: int | None = Field(default=None, description="The ID of th...")
    hreflang_inlink_urls: list[str | None] | None = Field(default=None)
    hreflang_inlink_urls_prev: list[str | None] | None = Field(default=None)
    hreflang_issues: list[str | None] | None = Field(default=None, description="The...")
    hreflang_issues_prev: list[str | None] | None = Field(default=None)
    hreflang_language: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_language_prev: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_link: list[str | None] | None = Field(default=None, description="The l...")
    hreflang_link_is_canonical: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_link_is_canonical_prev: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_link_prev: list[str | None] | None = Field(default=None)
    hreflang_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None)
    hreflang_pages_urls: list[str | None] | None = Field(default=None)
    hreflang_pages_urls_count: int | None = Field(default=None, description="Count ...")
    hreflang_pages_urls_count_diff: int | None = Field(default=None, description="C...")
    hreflang_pages_urls_count_prev: int | None = Field(default=None, description="C...")
    hreflang_pages_urls_prev: list[str | None] | None = Field(default=None)
    hreflang_prev: list[dict[str, Any] | None] | None = Field(default=None)
    html_lang: str | None = Field(default=None, description="Data from the page's H...")
    html_lang_code_is_valid: bool | None = Field(default=None, description="Indicat...")
    html_lang_code_is_valid_prev: bool | None = Field(default=None, description="In...")
    html_lang_country: str | None = Field(default=None, description="The region cod...")
    html_lang_country_prev: str | None = Field(default=None, description="The regio...")
    html_lang_language: str | None = Field(default=None, description="The language ...")
    html_lang_language_prev: str | None = Field(default=None, description="The lang...")
    html_lang_prev: str | None = Field(default=None, description="Data from the pag...")
    http_code: int | None = Field(default=None, description="The HTTP status code r...")
    http_header: list[str | None] | None = Field(default=None, description="The HTT...")
    http_header_prev: list[str | None] | None = Field(default=None, description="Th...")
    http_header_robots: list[str | None] | None = Field(default=None)
    http_header_robots_prev: list[str | None] | None = Field(default=None)
    http_headers_size: int | None = Field(default=None, description="The size of th...")
    http_headers_size_diff: int | None = Field(default=None, description="The size ...")
    http_headers_size_prev: int | None = Field(default=None, description="The size ...")
    images_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None)
    images_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None)
    incoming_all_links: int | None = Field(default=None, description="The number of...")
    incoming_all_links_diff: int | None = Field(default=None, description="The numb...")
    incoming_all_links_prev: int | None = Field(default=None, description="The numb...")
    incoming_canonical: int | None = Field(default=None, description="Shows how man...")
    incoming_canonical_diff: int | None = Field(default=None, description="Shows ho...")
    incoming_canonical_prev: int | None = Field(default=None, description="Shows ho...")
    incoming_css: int | None = Field(default=None, description="The number of incom...")
    incoming_css_diff: int | None = Field(default=None, description="The number of ...")
    incoming_css_prev: int | None = Field(default=None, description="The number of ...")
    incoming_follow: int | None = Field(default=None, description="The number of in...")
    incoming_follow_diff: int | None = Field(default=None, description="The number ...")
    incoming_follow_prev: int | None = Field(default=None, description="The number ...")
    incoming_hreflang: int | None = Field(default=None, description="Shows how many...")
    incoming_hreflang_diff: int | None = Field(default=None, description="Shows how...")
    incoming_hreflang_prev: int | None = Field(default=None, description="Shows how...")
    incoming_image: int | None = Field(default=None, description="The number of inc...")
    incoming_image_diff: int | None = Field(default=None, description="The number o...")
    incoming_image_prev: int | None = Field(default=None, description="The number o...")
    incoming_js: int | None = Field(default=None, description="The number of incomi...")
    incoming_js_diff: int | None = Field(default=None, description="The number of i...")
    incoming_js_prev: int | None = Field(default=None, description="The number of i...")
    incoming_links: int | None = Field(default=None, description="The number of inc...")
    incoming_links_diff: int | None = Field(default=None, description="The number o...")
    incoming_links_prev: int | None = Field(default=None, description="The number o...")
    incoming_nofollow: int | None = Field(default=None, description="The number of ...")
    incoming_nofollow_diff: int | None = Field(default=None, description="The numbe...")
    incoming_nofollow_prev: int | None = Field(default=None, description="The numbe...")
    incoming_pagination: int | None = Field(default=None, description="Shows how ma...")
    incoming_pagination_diff: int | None = Field(default=None, description="Shows h...")
    incoming_pagination_prev: int | None = Field(default=None, description="Shows h...")
    incoming_redirect: int | None = Field(default=None, description="The number of ...")
    incoming_redirect_diff: int | None = Field(default=None, description="The numbe...")
    incoming_redirect_prev: int | None = Field(default=None, description="The numbe...")
    indexnow_error: str | None = Field(default=None, description="The error descrip...")
    indexnow_error_prev: str | None = Field(default=None, description="The error de...")
    indexnow_reason: str | None = Field(default=None, description="The reason the p...")
    indexnow_reason_prev: str | None = Field(default=None, description="The reason ...")
    indexnow_status: str | None = Field(default=None, description="The status of In...")
    indexnow_status_prev: str | None = Field(default=None, description="The status ...")
    indexnow_submitted_at: str | None = Field(default=None, description="The date a...")
    indexnow_submitted_at_prev: str | None = Field(default=None, description="The d...")
    internal_code: list[dict[str, Any] | None] | None = Field(default=None)
    internal_inlink_urls: list[str | None] | None = Field(default=None)
    internal_inlink_urls_prev: list[str | None] | None = Field(default=None)
    internal_link_anchor: list[dict[str, Any] | None] | None = Field(default=None)
    internal_link_anchor_prev: list[dict[str, Any] | None] | None = Field(default=None)
    internal_link_domain: list[str | None] | None = Field(default=None)
    internal_link_domain_prev: list[str | None] | None = Field(default=None)
    internal_links: list[str | None] | None = Field(default=None, description="The ...")
    internal_links_is_canonical: list[dict[str, Any] | None] | None = Field(default=None)
    internal_links_is_canonical_prev: list[dict[str, Any] | None] | None = Field(default=None)
    internal_links_prev: list[str | None] | None = Field(default=None)
    internal_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None)
    internal_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None)
    internal_scheme: list[str | None] | None = Field(default=None, description="The...")
    internal_scheme_prev: list[str | None] | None = Field(default=None)
    is_html: bool | None = Field(default=None, description="Indicates that the cont...")
    is_in_sitemap: bool | None = Field(default=None, description="Indicates that th...")
    is_in_sitemap_prev: bool | None = Field(default=None, description="Indicates th...")
    is_page_title_used_in_serp: bool | None = Field(default=None, description="Indi...")
    is_redirect_loop: bool | None = Field(default=None, description="Checks if the ...")
    is_redirect_loop_prev: bool | None = Field(default=None, description="Checks if...")
    is_rendered: bool | None = Field(default=None, description="Indicates that the ...")
    is_rendered_prev: bool | None = Field(default=None, description="Indicates that...")
    is_valid_internal_html: bool | None = Field(default=None, description="The HTML...")
    is_valid_internal_html_prev: bool | None = Field(default=None, description="The...")
    js_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None)
    js_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None)
    jsonld_attributes: list[str | None] | None = Field(default=None, description="N...")
    jsonld_attributes_prev: list[str | None] | None = Field(default=None)
    jsonld_schema_types: list[str | None] | None = Field(default=None)
    jsonld_schema_types_prev: list[str | None] | None = Field(default=None)
    jsonld_validation_kinds: list[str | None] | None = Field(default=None)
    jsonld_validation_kinds_prev: list[str | None] | None = Field(default=None)
    jsonld_values: list[str | None] | None = Field(default=None, description="Value...")
    jsonld_values_prev: list[str | None] | None = Field(default=None)
    keywords: list[str | None] | None = Field(default=None, description="The page m...")
    keywords_prev: list[str | None] | None = Field(default=None, description="The p...")
    length: int | None = Field(default=None, description="The character length of t...")
    links_count_css: int | None = Field(default=None, description="The number of CS...")
    links_count_css_prev: int | None = Field(default=None, description="The number ...")
    links_count_external: int | None = Field(default=None, description="The number ...")
    links_count_external3xx: int | None = Field(default=None, description="The numb...")
    links_count_external3xx_diff: int | None = Field(default=None, description="The...")
    links_count_external3xx_prev: int | None = Field(default=None, description="The...")
    links_count_external4xx: int | None = Field(default=None, description="The numb...")
    links_count_external4xx_diff: int | None = Field(default=None, description="The...")
    links_count_external4xx_prev: int | None = Field(default=None, description="The...")
    links_count_external5xx: int | None = Field(default=None, description="The numb...")
    links_count_external5xx_diff: int | None = Field(default=None, description="The...")
    links_count_external5xx_prev: int | None = Field(default=None, description="The...")
    links_count_external_diff: int | None = Field(default=None, description="The nu...")
    links_count_external_follow: int | None = Field(default=None, description="The ...")
    links_count_external_follow_diff: int | None = Field(default=None)
    links_count_external_follow_prev: int | None = Field(default=None)
    links_count_external_nofollow: int | None = Field(default=None, description="Th...")
    links_count_external_nofollow_diff: int | None = Field(default=None)
    links_count_external_nofollow_prev: int | None = Field(default=None)
    links_count_external_non_canonical: int | None = Field(default=None)
    links_count_external_non_canonical_diff: int | None = Field(default=None)
    links_count_external_non_canonical_prev: int | None = Field(default=None)
    links_count_external_prev: int | None = Field(default=None, description="The nu...")
    links_count_external_xxx: int | None = Field(default=None, description="The num...")
    links_count_external_xxx_diff: int | None = Field(default=None, description="Th...")
    links_count_external_xxx_prev: int | None = Field(default=None, description="Th...")
    links_count_images: int | None = Field(default=None, description="The number of...")
    links_count_images_diff: int | None = Field(default=None, description="The numb...")
    links_count_images_prev: int | None = Field(default=None, description="The numb...")
    links_count_images_with_alt: int | None = Field(default=None, description="The ...")
    links_count_images_with_alt_diff: int | None = Field(default=None)
    links_count_images_with_alt_prev: int | None = Field(default=None)
    links_count_images_without_alt: int | None = Field(default=None, description="T...")
    links_count_images_without_alt_diff: int | None = Field(default=None)
    links_count_images_without_alt_prev: int | None = Field(default=None)
    links_count_internal: int | None = Field(default=None, description="The number ...")
    links_count_internal3xx: int | None = Field(default=None, description="The numb...")
    links_count_internal3xx_diff: int | None = Field(default=None, description="The...")
    links_count_internal3xx_prev: int | None = Field(default=None, description="The...")
    links_count_internal4xx: int | None = Field(default=None, description="The numb...")
    links_count_internal4xx_diff: int | None = Field(default=None, description="The...")
    links_count_internal4xx_prev: int | None = Field(default=None, description="The...")
    links_count_internal5xx: int | None = Field(default=None, description="The numb...")
    links_count_internal5xx_diff: int | None = Field(default=None, description="The...")
    links_count_internal5xx_prev: int | None = Field(default=None, description="The...")
    links_count_internal_diff: int | None = Field(default=None, description="The nu...")
    links_count_internal_follow: int | None = Field(default=None, description="The ...")
    links_count_internal_follow_diff: int | None = Field(default=None)
    links_count_internal_follow_prev: int | None = Field(default=None)
    links_count_internal_nofollow: int | None = Field(default=None, description="Th...")
    links_count_internal_nofollow_diff: int | None = Field(default=None)
    links_count_internal_nofollow_prev: int | None = Field(default=None)
    links_count_internal_non_canonical: int | None = Field(default=None)
    links_count_internal_non_canonical_diff: int | None = Field(default=None)
    links_count_internal_non_canonical_prev: int | None = Field(default=None)
    links_count_internal_prev: int | None = Field(default=None, description="The nu...")
    links_count_internal_xxx: int | None = Field(default=None, description="The num...")
    links_count_internal_xxx_diff: int | None = Field(default=None, description="Th...")
    links_count_internal_xxx_prev: int | None = Field(default=None, description="Th...")
    links_count_js: int | None = Field(default=None, description="The number of Jav...")
    links_count_js_diff: int | None = Field(default=None, description="The number o...")
    links_count_js_prev: int | None = Field(default=None, description="The number o...")
    links_css: list[str | None] | None = Field(default=None, description="The list ...")
    links_css_code: list[dict[str, Any] | None] | None = Field(default=None)
    links_css_domain: list[str | None] | None = Field(default=None, description="Th...")
    links_css_domain_prev: list[str | None] | None = Field(default=None)
    links_css_prev: list[str | None] | None = Field(default=None, description="The ...")
    links_css_scheme: list[str | None] | None = Field(default=None, description="Th...")
    links_css_scheme_prev: list[str | None] | None = Field(default=None)
    links_external3xx: list[str | None] | None = Field(default=None, description="T...")
    links_external3xx_prev: list[str | None] | None = Field(default=None)
    links_external4xx: list[str | None] | None = Field(default=None, description="T...")
    links_external4xx_prev: list[str | None] | None = Field(default=None)
    links_external5xx: list[str | None] | None = Field(default=None, description="T...")
    links_external5xx_prev: list[str | None] | None = Field(default=None)
    links_external_follow: list[str | None] | None = Field(default=None)
    links_external_follow_prev: list[str | None] | None = Field(default=None)
    links_external_nofollow: list[str | None] | None = Field(default=None)
    links_external_nofollow_prev: list[str | None] | None = Field(default=None)
    links_external_non_canonical: list[str | None] | None = Field(default=None)
    links_external_non_canonical_prev: list[str | None] | None = Field(default=None)
    links_external_xxx: list[str | None] | None = Field(default=None)
    links_external_xxx_prev: list[str | None] | None = Field(default=None)
    links_hreflang_code: list[dict[str, Any] | None] | None = Field(default=None)
    links_images: list[str | None] | None = Field(default=None, description="The li...")
    links_images_alt: list[dict[str, Any] | None] | None = Field(default=None)
    links_images_alt_prev: list[dict[str, Any] | None] | None = Field(default=None)
    links_images_code: list[dict[str, Any] | None] | None = Field(default=None)
    links_images_domain: list[str | None] | None = Field(default=None)
    links_images_domain_prev: list[str | None] | None = Field(default=None)
    links_images_prev: list[str | None] | None = Field(default=None, description="T...")
    links_images_scheme: list[str | None] | None = Field(default=None)
    links_images_scheme_prev: list[str | None] | None = Field(default=None)
    links_images_with_alt: list[str | None] | None = Field(default=None)
    links_images_with_alt_prev: list[str | None] | None = Field(default=None)
    links_images_without_alt: list[str | None] | None = Field(default=None)
    links_images_without_alt_prev: list[str | None] | None = Field(default=None)
    links_internal3xx: list[str | None] | None = Field(default=None, description="T...")
    links_internal3xx_prev: list[str | None] | None = Field(default=None)
    links_internal4xx: list[str | None] | None = Field(default=None, description="T...")
    links_internal4xx_prev: list[str | None] | None = Field(default=None)
    links_internal5xx: list[str | None] | None = Field(default=None, description="T...")
    links_internal5xx_prev: list[str | None] | None = Field(default=None)
    links_internal_follow: list[str | None] | None = Field(default=None)
    links_internal_follow_prev: list[str | None] | None = Field(default=None)
    links_internal_nofollow: list[str | None] | None = Field(default=None)
    links_internal_nofollow_prev: list[str | None] | None = Field(default=None)
    links_internal_non_canonical: list[str | None] | None = Field(default=None)
    links_internal_non_canonical_prev: list[str | None] | None = Field(default=None)
    links_internal_xxx: list[str | None] | None = Field(default=None)
    links_internal_xxx_prev: list[str | None] | None = Field(default=None)
    links_js: list[str | None] | None = Field(default=None, description="The list o...")
    links_js_code: list[dict[str, Any] | None] | None = Field(default=None)
    links_js_domain: list[str | None] | None = Field(default=None, description="The...")
    links_js_domain_prev: list[str | None] | None = Field(default=None)
    links_js_prev: list[str | None] | None = Field(default=None, description="The l...")
    links_js_scheme: list[str | None] | None = Field(default=None, description="The...")
    links_js_scheme_prev: list[str | None] | None = Field(default=None)
    loading_time: int | None = Field(default=None, description="The time it takes f...")
    loading_time_diff: int | None = Field(default=None, description="The time it ta...")
    loading_time_prev: int | None = Field(default=None, description="The time it ta...")
    meta_description: list[str | None] | None = Field(default=None, description="Me...")
    meta_description_length: list[int | None] | None = Field(default=None)
    meta_description_length_prev: list[int | None] | None = Field(default=None)
    meta_description_prev: list[str | None] | None = Field(default=None)
    meta_refresh: list[str | None] | None = Field(default=None, description="The ti...")
    meta_refresh_prev: list[str | None] | None = Field(default=None, description="T...")
    meta_robots: list[str | None] | None = Field(default=None, description="Instruc...")
    meta_robots_prev: list[str | None] | None = Field(default=None, description="In...")
    meta_twitter_tags_app_google_play: str | None = Field(default=None)
    meta_twitter_tags_app_google_play_prev: str | None = Field(default=None)
    meta_twitter_tags_app_ipad: str | None = Field(default=None, description="The a...")
    meta_twitter_tags_app_ipad_prev: str | None = Field(default=None)
    meta_twitter_tags_app_iphone: str | None = Field(default=None, description="The...")
    meta_twitter_tags_app_iphone_prev: str | None = Field(default=None)
    meta_twitter_tags_attributes: list[str | None] | None = Field(default=None)
    meta_twitter_tags_attributes_prev: list[str | None] | None = Field(default=None)
    meta_twitter_tags_card: str | None = Field(default=None, description="The X (Tw...")
    meta_twitter_tags_card_prev: str | None = Field(default=None, description="The ...")
    meta_twitter_tags_description: str | None = Field(default=None, description="me...")
    meta_twitter_tags_description_prev: str | None = Field(default=None)
    meta_twitter_tags_image: str | None = Field(default=None, description="The imag...")
    meta_twitter_tags_image_prev: str | None = Field(default=None, description="The...")
    meta_twitter_tags_image_url_invalid: bool | None = Field(default=None)
    meta_twitter_tags_image_url_invalid_prev: bool | None = Field(default=None)
    meta_twitter_tags_player: str | None = Field(default=None, description="The HTT...")
    meta_twitter_tags_player_height: int | None = Field(default=None)
    meta_twitter_tags_player_height_diff: int | None = Field(default=None)
    meta_twitter_tags_player_height_prev: int | None = Field(default=None)
    meta_twitter_tags_player_prev: str | None = Field(default=None, description="Th...")
    meta_twitter_tags_player_width: int | None = Field(default=None, description="T...")
    meta_twitter_tags_player_width_diff: int | None = Field(default=None)
    meta_twitter_tags_player_width_prev: int | None = Field(default=None)
    meta_twitter_tags_site: str | None = Field(default=None, description="The X (Tw...")
    meta_twitter_tags_site_prev: str | None = Field(default=None, description="The ...")
    meta_twitter_tags_title: str | None = Field(default=None, description="The titl...")
    meta_twitter_tags_title_prev: str | None = Field(default=None, description="The...")
    meta_twitter_tags_valid: bool | None = Field(default=None, description="Indicat...")
    meta_twitter_tags_valid_prev: bool | None = Field(default=None, description="In...")
    meta_twitter_tags_values: list[str | None] | None = Field(default=None)
    meta_twitter_tags_values_prev: list[str | None] | None = Field(default=None)
    navigation_next: str | None = Field(default=None, description="The URL specifie...")
    navigation_next_code: int | None = Field(default=None, description="The HTTP st...")
    navigation_next_no_crawl_reason: str | None = Field(default=None)
    navigation_next_no_crawl_reason_prev: str | None = Field(default=None)
    navigation_next_prev: str | None = Field(default=None, description="The URL spe...")
    navigation_prev_code: int | None = Field(default=None, description="The HTTP st...")
    navigation_prev_no_crawl_reason: str | None = Field(default=None)
    navigation_prev_no_crawl_reason_prev: str | None = Field(default=None)
    no_crawl_reason: str | None = Field(default=None, description="The reason why t...")
    no_crawl_reason_prev: str | None = Field(default=None, description="The reason ...")
    nofollow: int | None = Field(default=None, description="The number of incoming ...")
    nofollow_diff: int | None = Field(default=None, description="The number of inco...")
    nofollow_prev: int | None = Field(default=None, description="The number of inco...")
    nr_h1: int | None = Field(default=None, description="The number of H1 subheader...")
    nr_h1_prev: int | None = Field(default=None, description="The number of H1 subh...")
    nr_meta_description: int | None = Field(default=None, description="Number of Me...")
    nr_meta_description_diff: int | None = Field(default=None, description="Number ...")
    nr_meta_description_prev: int | None = Field(default=None, description="Number ...")
    nr_redirect_chain_urls: int | None = Field(default=None, description="The numbe...")
    nr_redirect_chain_urls_diff: int | None = Field(default=None, description="The ...")
    nr_redirect_chain_urls_prev: int | None = Field(default=None, description="The ...")
    nr_titles: int | None = Field(default=None, description="The number of title ta...")
    nr_titles_diff: int | None = Field(default=None, description="The number of tit...")
    nr_titles_prev: int | None = Field(default=None, description="The number of tit...")
    og_tags_attributes: list[str | None] | None = Field(default=None)
    og_tags_attributes_prev: list[str | None] | None = Field(default=None)
    og_tags_image: str | None = Field(default=None, description="The image URL spec...")
    og_tags_image_prev: str | None = Field(default=None, description="The image URL...")
    og_tags_image_url_invalid: bool | None = Field(default=None, description="Indic...")
    og_tags_image_url_invalid_prev: bool | None = Field(default=None)
    og_tags_inconsistent_canonical: bool | None = Field(default=None)
    og_tags_inconsistent_canonical_prev: bool | None = Field(default=None)
    og_tags_title: str | None = Field(default=None, description="The title text spe...")
    og_tags_title_prev: str | None = Field(default=None, description="The title tex...")
    og_tags_type: str | None = Field(default=None, description="The object type spe...")
    og_tags_type_prev: str | None = Field(default=None, description="The object typ...")
    og_tags_url: str | None = Field(default=None, description="The URL specified in...")
    og_tags_url_prev: str | None = Field(default=None, description="The URL specifi...")
    og_tags_url_valid: bool | None = Field(default=None, description="Indicates tha...")
    og_tags_url_valid_prev: bool | None = Field(default=None, description="Indicate...")
    og_tags_valid: bool | None = Field(default=None, description="Indicates that th...")
    og_tags_valid_prev: bool | None = Field(default=None, description="Indicates th...")
    og_tags_value: list[str | None] | None = Field(default=None, description="Data ...")
    og_tags_value_prev: list[str | None] | None = Field(default=None)
    origin: str | None = Field(default=None, description="Shows where the URL was o...")
    origin_prev: str | None = Field(default=None, description="Shows where the URL ...")
    page_is_nofollow: bool | None = Field(default=None, description="Check if the p...")
    page_is_nofollow_prev: bool | None = Field(default=None, description="Check if ...")
    page_is_noindex: bool | None = Field(default=None, description="Check if the pa...")
    page_is_noindex_prev: bool | None = Field(default=None, description="Check if t...")
    page_rating: int | None = Field(default=None, description="Page Rating (PR) sho...")
    page_raw_ur: int | None = Field(default=None, description="URL Rating (UR) show...")
    page_raw_ur_diff: int | None = Field(default=None, description="URL Rating (UR)...")
    page_raw_ur_prev: int | None = Field(default=None, description="URL Rating (UR)...")
    page_type: list[str | None] | None = Field(default=None, description="Site Audi...")
    page_type_prev: list[str | None] | None = Field(default=None, description="Site...")
    pagination_group: int | None = Field(default=None, description="The ID of the g...")
    pagination_group_prev: int | None = Field(default=None, description="The ID of ...")
    positions: int | None = Field(default=None, description="The number of keywords...")
    positions_diff: int | None = Field(default=None, description="The number of key...")
    positions_prev: int | None = Field(default=None, description="The number of key...")
    positions_top10: int | None = Field(default=None, description="The number of ke...")
    positions_top10_diff: int | None = Field(default=None, description="The number ...")
    positions_top10_prev: int | None = Field(default=None, description="The number ...")
    positions_top3: int | None = Field(default=None, description="The number of key...")
    positions_top3_diff: int | None = Field(default=None, description="The number o...")
    positions_top3_prev: int | None = Field(default=None, description="The number o...")
    psi_crux_cls_category: str | None = Field(default=None, description="Your CLS c...")
    psi_crux_cls_category_prev: str | None = Field(default=None, description="Your ...")
    psi_crux_cls_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_cls_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_cls_percentile: float | None = Field(default=None, description="Cumula...")
    psi_crux_cls_percentile_diff: int | None = Field(default=None, description="Cum...")
    psi_crux_cls_percentile_prev: float | None = Field(default=None, description="C...")
    psi_crux_fid_category: str | None = Field(default=None, description="Your FID c...")
    psi_crux_fid_category_prev: str | None = Field(default=None, description="Your ...")
    psi_crux_fid_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_fid_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_fid_percentile: float | None = Field(default=None, description="First ...")
    psi_crux_fid_percentile_diff: int | None = Field(default=None, description="Fir...")
    psi_crux_fid_percentile_prev: float | None = Field(default=None, description="F...")
    psi_crux_inp_category: str | None = Field(default=None, description="Your INP c...")
    psi_crux_inp_category_prev: str | None = Field(default=None, description="Your ...")
    psi_crux_inp_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_inp_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_inp_percentile: float | None = Field(default=None, description="Intera...")
    psi_crux_inp_percentile_diff: int | None = Field(default=None, description="Int...")
    psi_crux_inp_percentile_prev: float | None = Field(default=None, description="I...")
    psi_crux_lcp_category: str | None = Field(default=None, description="Your LCP c...")
    psi_crux_lcp_category_prev: str | None = Field(default=None, description="Your ...")
    psi_crux_lcp_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_lcp_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None)
    psi_crux_lcp_percentile: float | None = Field(default=None, description="Larges...")
    psi_crux_lcp_percentile_diff: int | None = Field(default=None, description="Lar...")
    psi_crux_lcp_percentile_prev: float | None = Field(default=None, description="L...")
    psi_lighthouse_cls_error_message: str | None = Field(default=None)
    psi_lighthouse_cls_error_message_prev: str | None = Field(default=None)
    psi_lighthouse_cls_value: float | None = Field(default=None, description="Cumul...")
    psi_lighthouse_cls_value_diff: int | None = Field(default=None, description="Cu...")
    psi_lighthouse_cls_value_prev: float | None = Field(default=None)
    psi_lighthouse_lcp_error_message: str | None = Field(default=None)
    psi_lighthouse_lcp_error_message_prev: str | None = Field(default=None)
    psi_lighthouse_lcp_value: float | None = Field(default=None, description="Large...")
    psi_lighthouse_lcp_value_diff: int | None = Field(default=None, description="La...")
    psi_lighthouse_lcp_value_prev: float | None = Field(default=None)
    psi_lighthouse_score: int | None = Field(default=None, description="This score ...")
    psi_lighthouse_score_diff: int | None = Field(default=None, description="This s...")
    psi_lighthouse_score_prev: int | None = Field(default=None, description="This s...")
    psi_lighthouse_tbt_error_message: str | None = Field(default=None)
    psi_lighthouse_tbt_error_message_prev: str | None = Field(default=None)
    psi_lighthouse_tbt_value: float | None = Field(default=None, description="Total...")
    psi_lighthouse_tbt_value_diff: int | None = Field(default=None, description="To...")
    psi_lighthouse_tbt_value_prev: float | None = Field(default=None)
    psi_mobile_issues: list[str | None] | None = Field(default=None, description="L...")
    psi_mobile_issues_explanations: list[str | None] | None = Field(default=None)
    psi_mobile_issues_explanations_prev: list[str | None] | None = Field(default=None)
    psi_mobile_issues_prev: list[str | None] | None = Field(default=None)
    psi_request_error_message: str | None = Field(default=None, description="The me...")
    psi_request_error_message_prev: str | None = Field(default=None, description="T...")
    psi_request_status: str | None = Field(default=None, description="The result of...")
    psi_request_status_prev: str | None = Field(default=None, description="The resu...")
    redirect: str | None = Field(default=None, description="The destination of the ...")
    redirect_chain_urls: list[str | None] | None = Field(default=None)
    redirect_chain_urls_code: list[dict[str, Any] | None] | None = Field(default=None)
    redirect_chain_urls_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None)
    redirect_chain_urls_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None)
    redirect_chain_urls_prev: list[str | None] | None = Field(default=None)
    redirect_code: int | None = Field(default=None, description="The HTTP status co...")
    redirect_counts: int | None = Field(default=None, description="The number of in...")
    redirect_counts_diff: int | None = Field(default=None, description="The number ...")
    redirect_counts_prev: int | None = Field(default=None, description="The number ...")
    redirect_is_canonical: bool | None = Field(default=None, description="Indicates...")
    redirect_is_canonical_prev: bool | None = Field(default=None, description="Indi...")
    redirect_no_crawl_reason: str | None = Field(default=None, description="The rea...")
    redirect_no_crawl_reason_prev: str | None = Field(default=None, description="Th...")
    redirect_prev: str | None = Field(default=None, description="The destination of...")
    redirect_scheme: str | None = Field(default=None, description="The protocol of ...")
    redirect_scheme_prev: str | None = Field(default=None, description="The protoco...")
    refclass_c: int | None = Field(default=None, description="The number of IP netw...")
    refclass_c_diff: int | None = Field(default=None, description="The number of IP...")
    refclass_c_prev: int | None = Field(default=None, description="The number of IP...")
    refhosts: int | None = Field(default=None, description="The number of unique ex...")
    refhosts_diff: int | None = Field(default=None, description="The number of uniq...")
    refhosts_prev: int | None = Field(default=None, description="The number of uniq...")
    refips: int | None = Field(default=None, description="The number of unique exte...")
    refips_prev: int | None = Field(default=None, description="The number of unique...")
    refpages: int | None = Field(default=None, description="The number of unique ex...")
    refpages_diff: int | None = Field(default=None, description="The number of uniq...")
    refpages_prev: int | None = Field(default=None, description="The number of uniq...")
    robots_allow_rules: list[dict[str, Any] | None] | None = Field(default=None)
    robots_allow_rules_prev: list[dict[str, Any] | None] | None = Field(default=None)
    robots_crawl_delay: int | None = Field(default=None, description="Crawl-delay:")
    robots_crawl_delay_prev: int | None = Field(default=None, description="Crawl-de...")
    robots_disallow_rules: list[dict[str, Any] | None] | None = Field(default=None)
    robots_disallow_rules_prev: list[dict[str, Any] | None] | None = Field(default=None)
    robots_error: str | None = Field(default=None, description="The error occurred ...")
    robots_error_prev: str | None = Field(default=None, description="The error occu...")
    robots_error_text: str | None = Field(default=None, description="Robots.txt err...")
    robots_error_text_prev: str | None = Field(default=None, description="Robots.tx...")
    robots_redirect_loop: list[dict[str, Any] | None] | None = Field(default=None)
    robots_redirect_loop_prev: list[dict[str, Any] | None] | None = Field(default=None)
    robots_sitemaps: list[dict[str, Any] | None] | None = Field(default=None)
    robots_sitemaps_prev: list[dict[str, Any] | None] | None = Field(default=None)
    rss: int | None = Field(default=None, description="The number of incoming exter...")
    rss_diff: int | None = Field(default=None, description="The number of incoming ...")
    rss_prev: int | None = Field(default=None, description="The number of incoming ...")
    scheme: str | None = Field(default=None, description="Hypertext Transfer Protoc...")
    self_canonical: bool | None = Field(default=None, description="Indicates that t...")
    self_canonical_prev: bool | None = Field(default=None, description="Indicates t...")
    self_hreflang: list[dict[str, Any] | None] | None = Field(default=None)
    self_hreflang_code_is_valid: list[dict[str, Any] | None] | None = Field(default=None)
    self_hreflang_code_is_valid_prev: list[dict[str, Any] | None] | None = Field(default=None)
    self_hreflang_country: list[dict[str, Any] | None] | None = Field(default=None)
    self_hreflang_country_prev: list[dict[str, Any] | None] | None = Field(default=None)
    self_hreflang_language: list[dict[str, Any] | None] | None = Field(default=None)
    self_hreflang_language_prev: list[dict[str, Any] | None] | None = Field(default=None)
    self_hreflang_prev: list[dict[str, Any] | None] | None = Field(default=None)
    serp_title: str | None = Field(default=None, description="The title displayed f...")
    serp_title_prev: str | None = Field(default=None, description="The title displa...")
    sitemap_error: str | None = Field(default=None, description="The error occurred...")
    sitemap_error_prev: str | None = Field(default=None, description="The error occ...")
    sitemap_error_text: str | None = Field(default=None, description="Sitemap error...")
    sitemap_error_text_prev: str | None = Field(default=None, description="Sitemap ...")
    sitemap_is_index: bool | None = Field(default=None, description="Indicates that...")
    sitemap_is_index_prev: bool | None = Field(default=None, description="Indicates...")
    sitemap_nr_urls: int | None = Field(default=None, description="The number of UR...")
    sitemap_nr_urls_prev: int | None = Field(default=None, description="The number ...")
    sitemap_save_max_size: int | None = Field(default=None, description="Max size o...")
    sitemap_save_max_size_diff: int | None = Field(default=None, description="Max s...")
    sitemap_save_max_size_prev: int | None = Field(default=None, description="Max s...")
    sitemap_unzipped_size: int | None = Field(default=None, description="Sitemap si...")
    sitemap_unzipped_size_diff: int | None = Field(default=None, description="Sitem...")
    sitemap_unzipped_size_prev: int | None = Field(default=None, description="Sitem...")
    size: int | None = Field(default=None, description="The size of the page or res...")
    size_diff: int | None = Field(default=None, description="The size of the page o...")
    size_prev: int | None = Field(default=None, description="The size of the page o...")
    source: list[str | None] | None = Field(default=None, description="Source from ...")
    source_prev: list[str | None] | None = Field(default=None, description="Source ...")
    stamp: str | None = Field(default=None, description="The time and date when the...")
    stamp_prev: str | None = Field(default=None, description="The time and date whe...")
    time_to_first_byte: int | None = Field(default=None, description="The time it t...")
    time_to_first_byte_prev: int | None = Field(default=None, description="The time...")
    title: list[str | None] | None = Field(default=None, description="The page title")
    title_prev: list[str | None] | None = Field(default=None, description="The page...")
    titles_length: list[int | None] | None = Field(default=None, description="The c...")
    titles_length_prev: list[int | None] | None = Field(default=None)
    top_keyword: str | None = Field(default=None, description="The keyword that bri...")
    top_keyword_position: int | None = Field(default=None, description="The positio...")
    top_keyword_position_diff: int | None = Field(default=None, description="The po...")
    top_keyword_position_prev: int | None = Field(default=None, description="The po...")
    top_keyword_prev: str | None = Field(default=None, description="The keyword tha...")
    traffic: float | None = Field(default=None, description="Our estimate of monthl...")
    traffic_diff: float | None = Field(default=None, description="Our estimate of m...")
    traffic_prev: float | None = Field(default=None, description="Our estimate of m...")
    url: str | None = Field(default=None, description="The web address of the page ...")
    url_prev: str | None = Field(default=None, description="The web address of the ...")

class SiteAuditPageExplorerResponse(BaseModel):
    """Response model for /page-explorer endpoint"""

    pages: list[SiteAuditPageExplorerData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteAuditPageExplorerData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-audit/projects
class SiteAuditProjectsRequest(BaseModel):
    """Request model for SiteAuditProjectsRequest."""

    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDT...")
    project_id: int | None = Field(default=None, description="The unique identifier...")

class SiteAuditProjectsData(BaseModel):
    """Individual data item for /projects endpoint"""

    project_id: str | None = Field(default=None, description="The unique identifier...")
    project_name: str | None = Field(default=None, description="The project name.")
    target_protocol: str | None = Field(default=None, description="The protocol of ...")
    target_url: str | None = Field(default=None, description="The URL of the projec...")
    target_mode: str | None = Field(default=None, description="The scope of the tar...")
    date: str | None = Field(default=None, description="The finish date and time of...")
    status: str | None = Field(default=None, description="The status of the most re...")
    health_score: int | None = Field(default=None, description="Reflects the propor...")
    urls_with_errors: int | None = Field(default=None, description="Number of inter...")
    urls_with_warnings: int | None = Field(default=None, description="Number of int...")
    urls_with_notices: int | None = Field(default=None, description="Number of inte...")
    total: int | None = Field(default=None, description="Number of total crawled in...")

class SiteAuditProjectsResponse(BaseModel):
    """Response model for /projects endpoint"""

    healthscores: list[SiteAuditProjectsData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteAuditProjectsData]:
        """Unwrap the response payload."""
        return self.healthscores or []


# ============== Site Explorer API ==============

# Models for site-explorer/all-backlinks
class SiteExplorerAllBacklinksRequest(BaseModel):
    """Request model for SiteExplorerAllBacklinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    aggregation: AggregationEnum = Field(default=AggregationEnum.SIMILAR_LINKS)
    history: str = Field(default="all_time", description="A time frame to add lost ...")

class SiteExplorerAllBacklinksData(BaseModel):
    """Individual data item for /all-backlinks endpoint"""

    ahrefs_rank_source: int | None = Field(default=None, description="The strength ...")
    ahrefs_rank_target: int | None = Field(default=None, description="The strength ...")
    alt: str | None = Field(default=None, description="The alt attribute of the link.")
    anchor: str | None = Field(default=None, description="The clickable words in a ...")
    broken_redirect_new_target: str | None = Field(default=None, description="The n...")
    broken_redirect_reason: BrokenRedirectReasonEnum | None = Field(default=None)
    broken_redirect_source: str | None = Field(default=None, description="The redir...")
    class_c: int | None = Field(default=None, description="(5 units) The number of ...")
    discovered_status: DiscoveredStatusEnum | None = Field(default=None)
    domain_rating_source: float | None = Field(default=None, description="The stren...")
    domain_rating_target: float | None = Field(default=None, description="The stren...")
    drop_reason: DropReasonEnum | None = Field(default=None, description="The reaso...")
    encoding: str | None = Field(default=None, description="The character set encod...")
    first_seen: str | None = Field(default=None, description="The date the referrin...")
    first_seen_link: str | None = Field(default=None, description="The date we firs...")
    http_code: int | None = Field(default=None, description="The return code from H...")
    http_crawl: bool | None = Field(default=None, description="The link was discove...")
    ip_source: str | None = Field(default=None, description="The referring domain I...")
    is_alternate: bool | None = Field(default=None, description="The link with the ...")
    is_canonical: bool | None = Field(default=None, description="The link with the ...")
    is_content: bool | None = Field(default=None, description="The link was found i...")
    is_dofollow: bool | None = Field(default=None, description="The link has no spe...")
    is_form: bool | None = Field(default=None, description="The link was found in a...")
    is_frame: bool | None = Field(default=None, description="The link was found in ...")
    is_image: bool | None = Field(default=None, description="The link is a regular ...")
    is_lost: bool | None = Field(default=None, description="The link currently does...")
    is_new: bool | None = Field(default=None, description="The link was discovered ...")
    is_nofollow: bool | None = Field(default=None, description="The link or the ref...")
    is_redirect: bool | None = Field(default=None, description="The link pointing t...")
    is_redirect_lost: bool | None = Field(default=None, description="The redirected...")
    is_root_source: bool | None = Field(default=None, description="The referring do...")
    is_root_target: bool | None = Field(default=None, description="The target domai...")
    is_rss: bool | None = Field(default=None, description="The link was found in an...")
    is_spam: bool | None = Field(default=None, description="Indicates whether the b...")
    is_sponsored: bool | None = Field(default=None, description="The link has the S...")
    is_text: bool | None = Field(default=None, description="The link is a standard ...")
    is_ugc: bool | None = Field(default=None, description="The link has the User Ge...")
    js_crawl: bool | None = Field(default=None, description="The link was discovere...")
    languages: list[str | None] | None = Field(default=None, description="The langu...")
    last_seen: str | None = Field(default=None, description="The date we discovered...")
    last_visited: str | None = Field(default=None, description="The date we last ve...")
    link_group_count: int | None = Field(default=None, description="The number of b...")
    link_type: LinkTypeEnum | None = Field(default=None, description="The kind of t...")
    linked_domains_source_domain: int | None = Field(default=None, description="The...")
    linked_domains_source_page: int | None = Field(default=None, description="The n...")
    linked_domains_target_domain: int | None = Field(default=None, description="The...")
    links_external: int | None = Field(default=None, description="The number of ext...")
    links_internal: int | None = Field(default=None, description="The number of int...")
    lost_reason: LostReasonEnum | None = Field(default=None, description="The reaso...")
    name_source: str | None = Field(default=None, description="The complete referri...")
    name_target: str | None = Field(default=None, description="The complete target ...")
    noindex: bool | None = Field(default=None, description="The referring page has ...")
    page_size: int | None = Field(default=None, description="The size in bytes of t...")
    port_source: int | None = Field(default=None, description="The network port of ...")
    port_target: int | None = Field(default=None, description="The network port of ...")
    positions: int | None = Field(default=None, description="The number of keywords...")
    powered_by: list[str | None] | None = Field(default=None, description="Web tech...")
    redirect_code: int | None = Field(default=None, description="The HTTP status co...")
    redirect_kind: list[int | None] | None = Field(default=None, description="The H...")
    refdomains_source: int | None = Field(default=None, description="(5 units) The ...")
    refdomains_source_domain: int | None = Field(default=None, description="(5 unit...")
    refdomains_target_domain: int | None = Field(default=None, description="(5 unit...")
    root_name_source: str | None = Field(default=None, description="The root domain...")
    root_name_target: str | None = Field(default=None, description="The root domain...")
    snippet_left: str | None = Field(default=None, description="The snippet of text...")
    snippet_right: str | None = Field(default=None, description="The snippet of tex...")
    source_page_author: str | None = Field(default=None, description="The author of...")
    source_page_publish_date: str | None = Field(default=None, description="the dat...")
    title: str | None = Field(default=None, description="The html title of the refe...")
    tld_class_source: TldClassSourceEnum | None = Field(default=None)
    tld_class_target: TldClassSourceEnum | None = Field(default=None)
    traffic: int | None = Field(default=None, description="(10 units) The referring...")
    traffic_domain: int | None = Field(default=None, description="(10 units) The re...")
    url_from: str | None = Field(default=None, description="The URL of the page con...")
    url_from_plain: str | None = Field(default=None, description="The referring pag...")
    url_rating_source: float | None = Field(default=None, description="The strength...")
    url_redirect: list[str | None] | None = Field(default=None, description="A redi...")
    url_redirect_with_target: list[str | None] | None = Field(default=None)
    url_to: str | None = Field(default=None, description="The URL the backlink poin...")
    url_to_plain: str | None = Field(default=None, description="The target page URL...")

class SiteExplorerAllBacklinksResponse(BaseModel):
    """Response model for /all-backlinks endpoint"""

    backlinks: list[SiteExplorerAllBacklinksData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerAllBacklinksData]:
        """Unwrap the response payload."""
        return self.backlinks or []


# Models for site-explorer/anchors
class SiteExplorerAnchorsRequest(BaseModel):
    """Request model for SiteExplorerAnchorsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    history: str = Field(default="all_time", description="A time frame to add lost ...")

class SiteExplorerAnchorsData(BaseModel):
    """Individual data item for /anchors endpoint"""

    anchor: str | None = Field(default=None, description="The clickable words in a ...")
    dofollow_links: int | None = Field(default=None, description="The number of lin...")
    first_seen: str | None = Field(default=None, description="The date we first fou...")
    is_spam: bool | None = Field(default=None, description="Indicates whether the b...")
    last_seen: str | None = Field(default=None, description="The date we discovered...")
    links_to_target: int | None = Field(default=None, description="The number of in...")
    lost_links: int | None = Field(default=None, description="The number of backlin...")
    new_links: int | None = Field(default=None, description="The number of new back...")
    refdomains: int | None = Field(default=None, description="(5 units) The number ...")
    refpages: int | None = Field(default=None, description="The number of pages con...")
    top_domain_rating: float | None = Field(default=None, description="The highest ...")

class SiteExplorerAnchorsResponse(BaseModel):
    """Response model for /anchors endpoint"""

    anchors: list[SiteExplorerAnchorsData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerAnchorsData]:
        """Unwrap the response payload."""
        return self.anchors or []


# Models for site-explorer/backlinks-stats
class SiteExplorerBacklinksStatsRequest(BaseModel):
    """Request model for SiteExplorerBacklinksStatsRequest."""

    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")

class SiteExplorerBacklinksStatsData(BaseModel):
    """Individual data item for /backlinks-stats endpoint"""

    live: int | None = Field(default=None, description="The total number of links f...")
    all_time: int | None = Field(default=None, description="The total number of lin...")
    live_refdomains: int | None = Field(default=None, description="(5 units) The to...")
    all_time_refdomains: int | None = Field(default=None, description="(5 units) Th...")

class SiteExplorerBacklinksStatsResponse(BaseModel):
    """Response model for /backlinks-stats endpoint"""

    metrics: SiteExplorerBacklinksStatsData | None = Field(default=None)

    @property
    def data(self) -> SiteExplorerBacklinksStatsData | None:
        """Unwrap the response payload."""
        return self.metrics


# Models for site-explorer/best-by-external-links
class SiteExplorerBestByExternalLinksRequest(BaseModel):
    """Request model for SiteExplorerBestByExternalLinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    history: str = Field(default="all_time", description="A time frame to add lost ...")

class SiteExplorerBestByExternalLinksData(BaseModel):
    """Individual data item for /best-by-external-links endpoint"""

    dofollow_to_target: int | None = Field(default=None, description="The number of...")
    first_seen_link: str | None = Field(default=None, description="The date we firs...")
    http_code_target: int | None = Field(default=None, description="The return code...")
    is_spam: bool | None = Field(default=None, description="Indicates whether the b...")
    languages_target: list[str | None] | None = Field(default=None, description="Th...")
    last_seen: str | None = Field(default=None, description="The date your target p...")
    last_visited_source: str | None = Field(default=None, description="The date we ...")
    last_visited_target: str | None = Field(default=None, description="The date we ...")
    links_to_target: int | None = Field(default=None, description="The number of in...")
    lost_links_to_target: int | None = Field(default=None, description="The number ...")
    new_links_to_target: int | None = Field(default=None, description="The number o...")
    nofollow_to_target: int | None = Field(default=None, description="The number of...")
    powered_by_target: list[str | None] | None = Field(default=None, description="W...")
    redirects_to_target: int | None = Field(default=None, description="The number o...")
    refdomains_target: int | None = Field(default=None, description="(5 units) The ...")
    target_redirect: str | None = Field(default=None, description="The target's red...")
    title_target: str | None = Field(default=None, description="The html title of t...")
    top_domain_rating_source: float | None = Field(default=None, description="The h...")
    url_rating_target: float | None = Field(default=None, description="The strength...")
    url_to: str | None = Field(default=None, description="The URL the backlink poin...")
    url_to_plain: str | None = Field(default=None, description="The target page URL...")

class SiteExplorerBestByExternalLinksResponse(BaseModel):
    """Response model for /best-by-external-links endpoint"""

    pages: list[SiteExplorerBestByExternalLinksData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerBestByExternalLinksData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/best-by-internal-links
class SiteExplorerBestByInternalLinksRequest(BaseModel):
    """Request model for SiteExplorerBestByInternalLinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerBestByInternalLinksData(BaseModel):
    """Individual data item for /best-by-internal-links endpoint"""

    canonical_to_target: int | None = Field(default=None, description="The number o...")
    dofollow_to_target: int | None = Field(default=None, description="The number of...")
    first_seen_link: str | None = Field(default=None, description="The date we firs...")
    http_code_target: int | None = Field(default=None, description="The return code...")
    languages_target: list[str | None] | None = Field(default=None, description="Th...")
    last_seen: str | None = Field(default=None, description="The date your target p...")
    last_visited_source: str | None = Field(default=None, description="The date we ...")
    last_visited_target: str | None = Field(default=None, description="The date we ...")
    links_to_target: int | None = Field(default=None, description="The number of in...")
    nofollow_to_target: int | None = Field(default=None, description="The number of...")
    powered_by_target: list[str | None] | None = Field(default=None, description="W...")
    redirects_to_target: int | None = Field(default=None, description="The number o...")
    target_redirect: str | None = Field(default=None, description="The target's red...")
    title_target: str | None = Field(default=None, description="The html title of t...")
    url_rating_target: float | None = Field(default=None, description="The strength...")
    url_to: str | None = Field(default=None, description="The URL the backlink poin...")
    url_to_plain: str | None = Field(default=None, description="The target page URL...")

class SiteExplorerBestByInternalLinksResponse(BaseModel):
    """Response model for /best-by-internal-links endpoint"""

    pages: list[SiteExplorerBestByInternalLinksData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerBestByInternalLinksData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/broken-backlinks
class SiteExplorerBrokenBacklinksRequest(BaseModel):
    """Request model for SiteExplorerBrokenBacklinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    aggregation: AggregationEnum = Field(default=AggregationEnum.SIMILAR_LINKS)

class SiteExplorerBrokenBacklinksData(BaseModel):
    """Individual data item for /broken-backlinks endpoint"""

    ahrefs_rank_source: int | None = Field(default=None, description="The strength ...")
    ahrefs_rank_target: int | None = Field(default=None, description="The strength ...")
    alt: str | None = Field(default=None, description="The alt attribute of the link.")
    anchor: str | None = Field(default=None, description="The clickable words in a ...")
    class_c: int | None = Field(default=None, description="(5 units) The number of ...")
    domain_rating_source: float | None = Field(default=None, description="The stren...")
    domain_rating_target: float | None = Field(default=None, description="The stren...")
    encoding: str | None = Field(default=None, description="The character set encod...")
    first_seen: str | None = Field(default=None, description="The date the referrin...")
    first_seen_link: str | None = Field(default=None, description="The date we firs...")
    http_code: int | None = Field(default=None, description="The return code from H...")
    http_code_target: int | None = Field(default=None, description="The return code...")
    http_crawl: bool | None = Field(default=None, description="The link was discove...")
    ip_source: str | None = Field(default=None, description="The referring domain I...")
    is_alternate: bool | None = Field(default=None, description="The link with the ...")
    is_canonical: bool | None = Field(default=None, description="The link with the ...")
    is_content: bool | None = Field(default=None, description="The link was found i...")
    is_dofollow: bool | None = Field(default=None, description="The link has no spe...")
    is_form: bool | None = Field(default=None, description="The link was found in a...")
    is_frame: bool | None = Field(default=None, description="The link was found in ...")
    is_image: bool | None = Field(default=None, description="The link is a regular ...")
    is_nofollow: bool | None = Field(default=None, description="The link or the ref...")
    is_redirect: bool | None = Field(default=None, description="The link pointing t...")
    is_root_source: bool | None = Field(default=None, description="The referring do...")
    is_root_target: bool | None = Field(default=None, description="The target domai...")
    is_rss: bool | None = Field(default=None, description="The link was found in an...")
    is_spam: bool | None = Field(default=None, description="Indicates whether the b...")
    is_sponsored: bool | None = Field(default=None, description="The link has the S...")
    is_text: bool | None = Field(default=None, description="The link is a standard ...")
    is_ugc: bool | None = Field(default=None, description="The link has the User Ge...")
    js_crawl: bool | None = Field(default=None, description="The link was discovere...")
    languages: list[str | None] | None = Field(default=None, description="The langu...")
    last_seen: str | None = Field(default=None, description="The date we discovered...")
    last_visited: str | None = Field(default=None, description="The date we last re...")
    last_visited_target: str | None = Field(default=None, description="The date we ...")
    link_group_count: int | None = Field(default=None, description="The number of b...")
    link_type: LinkTypeEnum | None = Field(default=None, description="The kind of t...")
    linked_domains_source_domain: int | None = Field(default=None, description="The...")
    linked_domains_source_page: int | None = Field(default=None, description="The n...")
    linked_domains_target_domain: int | None = Field(default=None, description="The...")
    links_external: int | None = Field(default=None, description="The number of ext...")
    links_internal: int | None = Field(default=None, description="The number of int...")
    name_source: str | None = Field(default=None, description="The complete referri...")
    name_target: str | None = Field(default=None, description="The complete target ...")
    page_size: int | None = Field(default=None, description="The size in bytes of t...")
    port_source: int | None = Field(default=None, description="The network port of ...")
    port_target: int | None = Field(default=None, description="The network port of ...")
    positions: int | None = Field(default=None, description="The number of keywords...")
    powered_by: list[str | None] | None = Field(default=None, description="Web tech...")
    redirect_code: int | None = Field(default=None, description="The HTTP status co...")
    redirect_kind: list[int | None] | None = Field(default=None, description="The H...")
    refdomains_source: int | None = Field(default=None, description="(5 units) The ...")
    refdomains_source_domain: int | None = Field(default=None, description="(5 unit...")
    refdomains_target_domain: int | None = Field(default=None, description="(5 unit...")
    root_name_source: str | None = Field(default=None, description="The root domain...")
    root_name_target: str | None = Field(default=None, description="The root domain...")
    snippet_left: str | None = Field(default=None, description="The snippet of text...")
    snippet_right: str | None = Field(default=None, description="The snippet of tex...")
    source_page_author: str | None = Field(default=None, description="The author of...")
    title: str | None = Field(default=None, description="The html title of the refe...")
    tld_class_source: TldClassSourceEnum | None = Field(default=None)
    tld_class_target: TldClassSourceEnum | None = Field(default=None)
    traffic: int | None = Field(default=None, description="(10 units) The referring...")
    traffic_domain: int | None = Field(default=None, description="(10 units) The re...")
    url_from: str | None = Field(default=None, description="The URL of the page con...")
    url_from_plain: str | None = Field(default=None, description="The referring pag...")
    url_rating_source: float | None = Field(default=None, description="The strength...")
    url_redirect: list[str | None] | None = Field(default=None, description="A redi...")
    url_redirect_with_target: list[str | None] | None = Field(default=None)
    url_to: str | None = Field(default=None, description="The URL the backlink poin...")
    url_to_plain: str | None = Field(default=None, description="The target page URL...")

class SiteExplorerBrokenBacklinksResponse(BaseModel):
    """Response model for /broken-backlinks endpoint"""

    backlinks: list[SiteExplorerBrokenBacklinksData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerBrokenBacklinksData]:
        """Unwrap the response payload."""
        return self.backlinks or []


# Models for site-explorer/domain-rating
class SiteExplorerDomainRatingRequest(BaseModel):
    """Request model for SiteExplorerDomainRatingRequest."""

    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")

class SiteExplorerDomainRatingData(BaseModel):
    """Individual data item for /domain-rating endpoint"""

    domain_rating: float | None = Field(default=None, description="The strength of ...")
    ahrefs_rank: int | None = Field(default=None, description="The strength of your...")

class SiteExplorerDomainRatingResponse(BaseModel):
    """Response model for /domain-rating endpoint"""

    domain_rating: SiteExplorerDomainRatingData | None = Field(default=None)

    @property
    def data(self) -> SiteExplorerDomainRatingData | None:
        """Unwrap the response payload."""
        return self.domain_rating


# Models for site-explorer/domain-rating-history
class SiteExplorerDomainRatingHistoryRequest(BaseModel):
    """Request model for SiteExplorerDomainRatingHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY)
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")

class SiteExplorerDomainRatingHistoryData(BaseModel):
    """Individual data item for /domain-rating-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    domain_rating: float | None = Field(default=None, description="The strength of ...")

class SiteExplorerDomainRatingHistoryResponse(BaseModel):
    """Response model for /domain-rating-history endpoint"""

    domain_ratings: list[SiteExplorerDomainRatingHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerDomainRatingHistoryData]:
        """Unwrap the response payload."""
        return self.domain_ratings or []


# Models for site-explorer/keywords-history
class SiteExplorerKeywordsHistoryRequest(BaseModel):
    """Request model for SiteExplorerKeywordsHistoryRequest."""

    select: SelectStr = Field(default="date,top3,top4_10,top11_plus")
    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY)
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerKeywordsHistoryData(BaseModel):
    """Individual data item for /keywords-history endpoint"""

    date: str | None = Field(default=None)
    top11_20: int | None = Field(default=None, description="The total number of key...")
    top11_plus: int | None = Field(default=None, description="The total number of k...")
    top21_50: int | None = Field(default=None, description="The total number of key...")
    top3: int | None = Field(default=None, description="The total number of keyword...")
    top4_10: int | None = Field(default=None, description="The total number of keyw...")
    top51_plus: int | None = Field(default=None, description="The total number of k...")

class SiteExplorerKeywordsHistoryResponse(BaseModel):
    """Response model for /keywords-history endpoint"""

    keywords: list[SiteExplorerKeywordsHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerKeywordsHistoryData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for site-explorer/linked-anchors-external
class SiteExplorerLinkedAnchorsExternalRequest(BaseModel):
    """Request model for SiteExplorerLinkedAnchorsExternalRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerLinkedAnchorsExternalData(BaseModel):
    """Individual data item for /linked-anchors-external endpoint"""

    anchor: str | None = Field(default=None, description="The clickable words in a ...")
    dofollow_links: int | None = Field(default=None, description="The number of out...")
    first_seen: str | None = Field(default=None, description="The date we first fou...")
    linked_domains: int | None = Field(default=None, description="The number of uni...")
    linked_pages: int | None = Field(default=None, description="The number of uniqu...")
    links_from_target: int | None = Field(default=None, description="The number of ...")

class SiteExplorerLinkedAnchorsExternalResponse(BaseModel):
    """Response model for /linked-anchors-external endpoint"""

    linkedanchors: list[SiteExplorerLinkedAnchorsExternalData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerLinkedAnchorsExternalData]:
        """Unwrap the response payload."""
        return self.linkedanchors or []


# Models for site-explorer/linked-anchors-internal
class SiteExplorerLinkedAnchorsInternalRequest(BaseModel):
    """Request model for SiteExplorerLinkedAnchorsInternalRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerLinkedAnchorsInternalData(BaseModel):
    """Individual data item for /linked-anchors-internal endpoint"""

    anchor: str | None = Field(default=None, description="The clickable words in a ...")
    dofollow_links: int | None = Field(default=None, description="The number of out...")
    first_seen: str | None = Field(default=None, description="The date we first fou...")
    linked_pages: int | None = Field(default=None, description="The number of uniqu...")
    links_from_target: int | None = Field(default=None, description="The number of ...")

class SiteExplorerLinkedAnchorsInternalResponse(BaseModel):
    """Response model for /linked-anchors-internal endpoint"""

    linkedanchors: list[SiteExplorerLinkedAnchorsInternalData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerLinkedAnchorsInternalData]:
        """Unwrap the response payload."""
        return self.linkedanchors or []


# Models for site-explorer/linkeddomains
class SiteExplorerLinkeddomainsRequest(BaseModel):
    """Request model for SiteExplorerLinkeddomainsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerLinkeddomainsData(BaseModel):
    """Individual data item for /linkeddomains endpoint"""

    dofollow_linked_domains: int | None = Field(default=None, description="The numb...")
    dofollow_links: int | None = Field(default=None, description="The number of lin...")
    dofollow_refdomains: int | None = Field(default=None, description="(5 units) Th...")
    domain: str | None = Field(default=None, description="A linked domain that has ...")
    domain_rating: float | None = Field(default=None, description="The strength of ...")
    first_seen: str | None = Field(default=None, description="The date we first fou...")
    is_root_domain: bool | None = Field(default=None, description="The domain name ...")
    linked_domain_traffic: int | None = Field(default=None, description="(10 units)...")
    linked_pages: int | None = Field(default=None, description="The number of the d...")
    links_from_target: int | None = Field(default=None, description="The number of ...")

class SiteExplorerLinkeddomainsResponse(BaseModel):
    """Response model for /linkeddomains endpoint"""

    linkeddomains: list[SiteExplorerLinkeddomainsData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerLinkeddomainsData]:
        """Unwrap the response payload."""
        return self.linkeddomains or []


# Models for site-explorer/metrics
class SiteExplorerMetricsRequest(BaseModel):
    """Request model for SiteExplorerMetricsRequest."""

    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")

class SiteExplorerMetricsData(BaseModel):
    """Individual data item for /metrics endpoint"""

    org_keywords: int | None = Field(default=None, description="The total number of...")
    paid_keywords: int | None = Field(default=None, description="The total number o...")
    org_keywords_1_3: int | None = Field(default=None, description="The total numbe...")
    org_traffic: int | None = Field(default=None, description="(10 units) The estim...")
    org_cost: int | None = Field(default=None, description="(10 units) The estimate...")
    paid_traffic: int | None = Field(default=None, description="(10 units) The esti...")
    paid_cost: int | None = Field(default=None, description="(10 units) The estimat...")
    paid_pages: int | None = Field(default=None, description="The total number of p...")

class SiteExplorerMetricsResponse(BaseModel):
    """Response model for /metrics endpoint"""

    metrics: SiteExplorerMetricsData | None = Field(default=None, description="The ...")

    @property
    def data(self) -> SiteExplorerMetricsData | None:
        """Unwrap the response payload."""
        return self.metrics


# Models for site-explorer/metrics-by-country
class SiteExplorerMetricsByCountryRequest(BaseModel):
    """Request model for SiteExplorerMetricsByCountryRequest."""

    select: SelectStr = Field(default="paid_cost,paid_keywords,org_cost,paid_pages,org_keywords_1_3,org_keywords,org_traffic,paid_traffic,country")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")

class SiteExplorerMetricsByCountryData(BaseModel):
    """Individual data item for /metrics-by-country endpoint"""

    country: CountryEnum1 | None = Field(default=None, description="The country field")
    org_cost: int | None = Field(default=None, description="(10 units) The estimate...")
    org_keywords: int | None = Field(default=None, description="The total number of...")
    org_keywords_1_3: int | None = Field(default=None, description="The total numbe...")
    org_traffic: int | None = Field(default=None, description="(10 units) The estim...")
    paid_cost: int | None = Field(default=None, description="(10 units) The estimat...")
    paid_keywords: int | None = Field(default=None, description="The total number o...")
    paid_pages: int | None = Field(default=None, description="The total number of p...")
    paid_traffic: int | None = Field(default=None, description="(10 units) The esti...")

class SiteExplorerMetricsByCountryResponse(BaseModel):
    """Response model for /metrics-by-country endpoint"""

    metrics: list[SiteExplorerMetricsByCountryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerMetricsByCountryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for site-explorer/metrics-history
class SiteExplorerMetricsHistoryRequest(BaseModel):
    """Request model for SiteExplorerMetricsHistoryRequest."""

    select: SelectStr = Field(default="date,org_cost,org_traffic,paid_cost,paid_traffic")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)
    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY)
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerMetricsHistoryData(BaseModel):
    """Individual data item for /metrics-history endpoint"""

    date: str | None = Field(default=None)
    org_cost: int | None = Field(default=None, description="(10 units) The estimate...")
    org_traffic: int | None = Field(default=None, description="(10 units) The estim...")
    paid_cost: int | None = Field(default=None, description="(10 units) The estimat...")
    paid_traffic: int | None = Field(default=None, description="(10 units) The esti...")

class SiteExplorerMetricsHistoryResponse(BaseModel):
    """Response model for /metrics-history endpoint"""

    metrics: list[SiteExplorerMetricsHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerMetricsHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for site-explorer/organic-competitors
class SiteExplorerOrganicCompetitorsRequest(BaseModel):
    """Request model for SiteExplorerOrganicCompetitorsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3...")
    date_compared: DateStr | None = Field(default=None, description="A date to comp...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class SiteExplorerOrganicCompetitorsData(BaseModel):
    """Individual data item for /organic-competitors endpoint"""

    competitor_domain: str | None = Field(default=None, description="A competitor's...")
    competitor_url: str | None = Field(default=None, description="A competitor's UR...")
    domain_rating: float | None = Field(default=None, description="The strength of ...")
    group_mode: GroupModeEnum | None = Field(default=None, description="To see comp...")
    keywords_common: int | None = Field(default=None, description="Organic keywords...")
    keywords_competitor: int | None = Field(default=None, description="Organic keyw...")
    keywords_target: int | None = Field(default=None, description="Organic keywords...")
    pages: int | None = Field(default=None, description="The total number of pages ...")
    pages_diff: int | None = Field(default=None, description="The change in pages b...")
    pages_merged: int | None = Field(default=None, description="The pages field opt...")
    pages_prev: int | None = Field(default=None, description="The total number of p...")
    share: float | None = Field(default=None, description="The percentage of common...")
    traffic: int | None = Field(default=None, description="(10 units) An estimation...")
    traffic_diff: int | None = Field(default=None, description="The change in traff...")
    traffic_merged: int | None = Field(default=None, description="(10 units) The tr...")
    traffic_prev: int | None = Field(default=None, description="(10 units) An estim...")
    value: int | None = Field(default=None, description="(10 units) The estimated v...")
    value_diff: int | None = Field(default=None, description="The change in value b...")
    value_merged: int | None = Field(default=None, description="(10 units) The valu...")
    value_prev: int | None = Field(default=None, description="(10 units) The estima...")

class SiteExplorerOrganicCompetitorsResponse(BaseModel):
    """Response model for /organic-competitors endpoint"""

    competitors: list[SiteExplorerOrganicCompetitorsData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerOrganicCompetitorsData]:
        """Unwrap the response payload."""
        return self.competitors or []


# Models for site-explorer/organic-keywords
class SiteExplorerOrganicKeywordsRequest(BaseModel):
    """Request model for SiteExplorerOrganicKeywordsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    date_compared: DateStr | None = Field(default=None, description="A date to comp...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class SiteExplorerOrganicKeywordsData(BaseModel):
    """Individual data item for /organic-keywords endpoint"""

    all_positions: list[dict[str, Any] | None] | None = Field(default=None)
    all_positions_prev: list[dict[str, Any] | None] | None = Field(default=None)
    best_position: int | None = Field(default=None, description="The top position y...")
    best_position_diff: int | None = Field(default=None, description="The change in...")
    best_position_has_thumbnail: bool | None = Field(default=None, description="The...")
    best_position_has_thumbnail_prev: bool | None = Field(default=None)
    best_position_has_video: bool | None = Field(default=None, description="The top...")
    best_position_has_video_prev: bool | None = Field(default=None, description="Th...")
    best_position_kind: BestPositionKindEnum | None = Field(default=None)
    best_position_kind_merged: BestPositionKindEnum | None = Field(default=None)
    best_position_kind_prev: BestPositionKindEnum | None = Field(default=None)
    best_position_prev: int | None = Field(default=None, description="The top posit...")
    best_position_set: BestPositionSetEnum | None = Field(default=None)
    best_position_set_prev: BestPositionSetEnum | None = Field(default=None)
    best_position_url: str | None = Field(default=None, description="The ranking UR...")
    best_position_url_prev: str | None = Field(default=None, description="The ranki...")
    cpc: int | None = Field(default=None, description="Cost Per Click shows the ave...")
    cpc_merged: int | None = Field(default=None, description="The CPC field optimiz...")
    cpc_prev: int | None = Field(default=None, description="The CPC metric on the c...")
    entities: list[dict[str, Any] | None] | None = Field(default=None)
    is_best_position_set_top_11_50: bool | None = Field(default=None)
    is_best_position_set_top_11_50_prev: bool | None = Field(default=None)
    is_best_position_set_top_3: bool | None = Field(default=None, description="The ...")
    is_best_position_set_top_3_prev: bool | None = Field(default=None)
    is_best_position_set_top_4_10: bool | None = Field(default=None, description="T...")
    is_best_position_set_top_4_10_prev: bool | None = Field(default=None)
    is_branded: bool | None = Field(default=None, description="User intent: branded...")
    is_commercial: bool | None = Field(default=None, description="User intent: comm...")
    is_informational: bool | None = Field(default=None, description="User intent: i...")
    is_local: bool | None = Field(default=None, description="User intent: local. Th...")
    is_navigational: bool | None = Field(default=None, description="User intent: na...")
    is_transactional: bool | None = Field(default=None, description="User intent: t...")
    keyword: str | None = Field(default=None, description="The keyword your target ...")
    keyword_country: CountryEnum1 | None = Field(default=None, description="The cou...")
    keyword_difficulty: int | None = Field(default=None, description="(10 units) An...")
    keyword_difficulty_merged: int | None = Field(default=None, description="(10 un...")
    keyword_difficulty_prev: int | None = Field(default=None, description="(10 unit...")
    keyword_merged: str | None = Field(default=None, description="The keyword field...")
    keyword_prev: str | None = Field(default=None, description="The keyword your ta...")
    language: str | None = Field(default=None, description="The SERP language.")
    language_prev: str | None = Field(default=None, description="The SERP language ...")
    last_update: str | None = Field(default=None, description="The date when we las...")
    last_update_prev: str | None = Field(default=None, description="The date when w...")
    serp_features: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None)
    serp_features_count: int | None = Field(default=None, description="The number o...")
    serp_features_count_prev: int | None = Field(default=None, description="The num...")
    serp_features_merged: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None)
    serp_features_prev: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None)
    serp_target_main_positions_count: int | None = Field(default=None)
    serp_target_main_positions_count_prev: int | None = Field(default=None)
    serp_target_positions_count: int | None = Field(default=None, description="The ...")
    serp_target_positions_count_prev: int | None = Field(default=None)
    status: StatusEnum | None = Field(default=None, description="The status of a pa...")
    sum_paid_traffic: int | None = Field(default=None, description="(10 units) An e...")
    sum_paid_traffic_merged: int | None = Field(default=None, description="(10 unit...")
    sum_paid_traffic_prev: int | None = Field(default=None, description="(10 units)...")
    sum_traffic: int | None = Field(default=None, description="(10 units) An estima...")
    sum_traffic_merged: int | None = Field(default=None, description="(10 units) Th...")
    sum_traffic_prev: int | None = Field(default=None, description="(10 units) The ...")
    volume: int | None = Field(default=None, description="(10 units) An estimation ...")
    volume_desktop_pct: float | None = Field(default=None, description="The percent...")
    volume_merged: int | None = Field(default=None, description="(10 units) The sea...")
    volume_mobile_pct: float | None = Field(default=None, description="The percenta...")
    volume_prev: int | None = Field(default=None, description="(10 units) The searc...")
    words: int | None = Field(default=None, description="The number of words in a k...")
    words_merged: int | None = Field(default=None, description="The number of words...")
    words_prev: int | None = Field(default=None, description="The number of words i...")

class SiteExplorerOrganicKeywordsResponse(BaseModel):
    """Response model for /organic-keywords endpoint"""

    keywords: list[SiteExplorerOrganicKeywordsData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerOrganicKeywordsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for site-explorer/outlinks-stats
class SiteExplorerOutlinksStatsRequest(BaseModel):
    """Request model for SiteExplorerOutlinksStatsRequest."""

    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")

class SiteExplorerOutlinksStatsData(BaseModel):
    """Individual data item for /outlinks-stats endpoint"""

    outgoing_links: int | None = Field(default=None, description="The number of ext...")
    outgoing_links_dofollow: int | None = Field(default=None, description="The numb...")
    linked_domains: int | None = Field(default=None, description="The number of uni...")
    linked_domains_dofollow: int | None = Field(default=None, description="The numb...")

class SiteExplorerOutlinksStatsResponse(BaseModel):
    """Response model for /outlinks-stats endpoint"""

    metrics: SiteExplorerOutlinksStatsData | None = Field(default=None)

    @property
    def data(self) -> SiteExplorerOutlinksStatsData | None:
        """Unwrap the response payload."""
        return self.metrics


# Models for site-explorer/pages-by-traffic
class SiteExplorerPagesByTrafficRequest(BaseModel):
    """Request model for SiteExplorerPagesByTrafficRequest."""

    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerPagesByTrafficData(BaseModel):
    """Individual data item for /pages-by-traffic endpoint"""

    range0_pages: int | None = Field(default=None, description="The total number of...")
    range100_traffic: int | None = Field(default=None, description="(10 units) The ...")
    range100_pages: int | None = Field(default=None, description="The total number ...")
    range1k_traffic: int | None = Field(default=None, description="(10 units) The t...")
    range1k_pages: int | None = Field(default=None, description="The total number o...")
    range5k_traffic: int | None = Field(default=None, description="(10 units) The t...")
    range5k_pages: int | None = Field(default=None, description="The total number o...")
    range10k_traffic: int | None = Field(default=None, description="(10 units) The ...")
    range10k_pages: int | None = Field(default=None, description="The total number ...")
    range10k_plus_traffic: int | None = Field(default=None, description="(10 units)...")
    range10k_plus_pages: int | None = Field(default=None, description="The total nu...")

class SiteExplorerPagesByTrafficResponse(BaseModel):
    """Response model for /pages-by-traffic endpoint"""

    pages: SiteExplorerPagesByTrafficData | None = Field(default=None)

    @property
    def data(self) -> SiteExplorerPagesByTrafficData | None:
        """Unwrap the response payload."""
        return self.pages


# Models for site-explorer/pages-history
class SiteExplorerPagesHistoryRequest(BaseModel):
    """Request model for SiteExplorerPagesHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY)
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerPagesHistoryData(BaseModel):
    """Individual data item for /pages-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    pages: int | None = Field(default=None, description="The total number of pages ...")

class SiteExplorerPagesHistoryResponse(BaseModel):
    """Response model for /pages-history endpoint"""

    pages: list[SiteExplorerPagesHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerPagesHistoryData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/paid-pages
class SiteExplorerPaidPagesRequest(BaseModel):
    """Request model for SiteExplorerPaidPagesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    date_compared: DateStr | None = Field(default=None, description="A date to comp...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class SiteExplorerPaidPagesData(BaseModel):
    """Individual data item for /paid-pages endpoint"""

    ads_count: int | None = Field(default=None, description="The number of unique a...")
    ads_count_diff: int | None = Field(default=None, description="The change in ads...")
    ads_count_prev: int | None = Field(default=None, description="The number of ads...")
    keywords: int | None = Field(default=None, description="The total number of key...")
    keywords_diff: int | None = Field(default=None, description="The change in keyw...")
    keywords_diff_percent: int | None = Field(default=None, description="The change...")
    keywords_merged: int | None = Field(default=None, description="The total number...")
    keywords_prev: int | None = Field(default=None, description="The keyword your t...")
    raw_url: str | None = Field(default=None, description="The ranking page URL in ...")
    raw_url_prev: str | None = Field(default=None, description="The ranking page UR...")
    referring_domains: int | None = Field(default=None, description="(5 units) The ...")
    status: StatusEnum | None = Field(default=None, description="The status of a pa...")
    sum_traffic: int | None = Field(default=None, description="(10 units) An estima...")
    sum_traffic_merged: int | None = Field(default=None, description="(10 units) Th...")
    sum_traffic_prev: int | None = Field(default=None, description="(10 units) The ...")
    top_keyword: str | None = Field(default=None, description="The keyword that bri...")
    top_keyword_best_position: int | None = Field(default=None, description="The ra...")
    top_keyword_best_position_diff: int | None = Field(default=None, description="T...")
    top_keyword_best_position_kind: BestPositionKindEnum | None = Field(default=None)
    top_keyword_best_position_kind_prev: BestPositionKindEnum | None = Field(default=None)
    top_keyword_best_position_prev: int | None = Field(default=None, description="T...")
    top_keyword_best_position_title: str | None = Field(default=None)
    top_keyword_best_position_title_prev: str | None = Field(default=None)
    top_keyword_country: CountryEnum1 | None = Field(default=None, description="The...")
    top_keyword_country_prev: CountryEnum1 | None = Field(default=None)
    top_keyword_prev: str | None = Field(default=None, description="The keyword tha...")
    top_keyword_volume: int | None = Field(default=None, description="(10 units) An...")
    top_keyword_volume_prev: int | None = Field(default=None, description="(10 unit...")
    traffic_diff: int | None = Field(default=None, description="The change in traff...")
    traffic_diff_percent: int | None = Field(default=None, description="The change ...")
    ur: float | None = Field(default=None, description="URL Rating (UR) shows the s...")
    url: str | None = Field(default=None, description="The ranking page URL.")
    url_prev: str | None = Field(default=None, description="The ranking page URL on...")
    value: int | None = Field(default=None, description="(10 units) The estimated c...")
    value_diff: int | None = Field(default=None, description="The change in traffic...")
    value_diff_percent: int | None = Field(default=None, description="The change in...")
    value_merged: int | None = Field(default=None, description="(10 units) The traf...")
    value_prev: int | None = Field(default=None, description="(10 units) The traffi...")

class SiteExplorerPaidPagesResponse(BaseModel):
    """Response model for /paid-pages endpoint"""

    pages: list[SiteExplorerPaidPagesData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerPaidPagesData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/refdomains
class SiteExplorerRefdomainsRequest(BaseModel):
    """Request model for SiteExplorerRefdomainsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    history: str = Field(default="all_time", description="A time frame to add lost ...")

class SiteExplorerRefdomainsData(BaseModel):
    """Individual data item for /refdomains endpoint"""

    dofollow_linked_domains: int | None = Field(default=None, description="The numb...")
    dofollow_links: int | None = Field(default=None, description="The number of lin...")
    dofollow_refdomains: int | None = Field(default=None, description="(5 units) Th...")
    domain: str | None = Field(default=None, description="A referring domain that h...")
    domain_rating: float | None = Field(default=None, description="The strength of ...")
    first_seen: str | None = Field(default=None, description="The date we first fou...")
    ip_source: str | None = Field(default=None, description="The referring domain I...")
    is_root_domain: bool | None = Field(default=None, description="The domain name ...")
    is_spam: bool | None = Field(default=None, description="Indicates whether the b...")
    last_seen: str | None = Field(default=None, description="The date your target l...")
    links_to_target: int | None = Field(default=None, description="The number of ba...")
    lost_links: int | None = Field(default=None, description="The number of backlin...")
    new_links: int | None = Field(default=None, description="The number of new back...")
    positions_source_domain: int | None = Field(default=None, description="The numb...")
    traffic_domain: int | None = Field(default=None, description="(10 units) The re...")

class SiteExplorerRefdomainsResponse(BaseModel):
    """Response model for /refdomains endpoint"""

    refdomains: list[SiteExplorerRefdomainsData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerRefdomainsData]:
        """Unwrap the response payload."""
        return self.refdomains or []


# Models for site-explorer/refdomains-history
class SiteExplorerRefdomainsHistoryRequest(BaseModel):
    """Request model for SiteExplorerRefdomainsHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY)
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerRefdomainsHistoryData(BaseModel):
    """Individual data item for /refdomains-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    refdomains: int | None = Field(default=None, description="(5 units) The total n...")

class SiteExplorerRefdomainsHistoryResponse(BaseModel):
    """Response model for /refdomains-history endpoint"""

    refdomains: list[SiteExplorerRefdomainsHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerRefdomainsHistoryData]:
        """Unwrap the response payload."""
        return self.refdomains or []


# Models for site-explorer/top-pages
class SiteExplorerTopPagesRequest(BaseModel):
    """Request model for SiteExplorerTopPagesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duratio...")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order resul...")
    where: str | None = Field(default=None, description="The filter expression. The...")
    select: SelectStr = Field(..., description="A comma-separated list of columns t...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    date_compared: DateStr | None = Field(default=None, description="A date to comp...")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-...")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)

class SiteExplorerTopPagesData(BaseModel):
    """Individual data item for /top-pages endpoint"""

    keywords: int | None = Field(default=None, description="The total number of key...")
    keywords_diff: int | None = Field(default=None, description="The change in keyw...")
    keywords_diff_percent: int | None = Field(default=None, description="The change...")
    keywords_merged: int | None = Field(default=None, description="The total number...")
    keywords_prev: int | None = Field(default=None, description="The keyword your t...")
    raw_url: str | None = Field(default=None, description="The ranking page URL in ...")
    raw_url_prev: str | None = Field(default=None, description="The ranking page UR...")
    referring_domains: int | None = Field(default=None, description="(5 units) The ...")
    status: StatusEnum | None = Field(default=None, description="The status of a pa...")
    sum_traffic: int | None = Field(default=None, description="(10 units) An estima...")
    sum_traffic_merged: int | None = Field(default=None, description="(10 units) Th...")
    sum_traffic_prev: int | None = Field(default=None, description="(10 units) The ...")
    top_keyword: str | None = Field(default=None, description="The keyword that bri...")
    top_keyword_best_position: int | None = Field(default=None, description="The ra...")
    top_keyword_best_position_diff: int | None = Field(default=None, description="T...")
    top_keyword_best_position_kind: BestPositionKindEnum | None = Field(default=None)
    top_keyword_best_position_kind_prev: BestPositionKindEnum | None = Field(default=None)
    top_keyword_best_position_prev: int | None = Field(default=None, description="T...")
    top_keyword_best_position_title: str | None = Field(default=None)
    top_keyword_best_position_title_prev: str | None = Field(default=None)
    top_keyword_country: CountryEnum1 | None = Field(default=None, description="The...")
    top_keyword_country_prev: CountryEnum1 | None = Field(default=None)
    top_keyword_prev: str | None = Field(default=None, description="The keyword tha...")
    top_keyword_volume: int | None = Field(default=None, description="(10 units) An...")
    top_keyword_volume_prev: int | None = Field(default=None, description="(10 unit...")
    traffic_diff: int | None = Field(default=None, description="The change in traff...")
    traffic_diff_percent: int | None = Field(default=None, description="The change ...")
    ur: float | None = Field(default=None, description="URL Rating (UR) shows the s...")
    url: str | None = Field(default=None, description="The ranking page URL.")
    url_prev: str | None = Field(default=None, description="The ranking page URL on...")
    value: int | None = Field(default=None, description="(10 units) The estimated v...")
    value_diff: int | None = Field(default=None, description="The change in traffic...")
    value_diff_percent: int | None = Field(default=None, description="The change in...")
    value_merged: int | None = Field(default=None, description="(10 units) The traf...")
    value_prev: int | None = Field(default=None, description="(10 units) The traffi...")

class SiteExplorerTopPagesResponse(BaseModel):
    """Response model for /top-pages endpoint"""

    pages: list[SiteExplorerTopPagesData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerTopPagesData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/total-search-volume-history
class SiteExplorerTotalSearchVolumeHistoryRequest(BaseModel):
    """Request model for SiteExplorerTotalSearchVolumeHistoryRequest."""

    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY)
    top_positions: ViewForEnum = Field(default=ViewForEnum.TOP_10, description="The...")
    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY)
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    country: CountryEnum | None = Field(default=None, description="A two-letter cou...")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The prot...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of t...")

class SiteExplorerTotalSearchVolumeHistoryData(BaseModel):
    """Individual data item for /total-search-volume-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    total_search_volume: int | None = Field(default=None, description="(10 units) T...")

class SiteExplorerTotalSearchVolumeHistoryResponse(BaseModel):
    """Response model for /total-search-volume-history endpoint"""

    metrics: list[SiteExplorerTotalSearchVolumeHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerTotalSearchVolumeHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for site-explorer/url-rating-history
class SiteExplorerUrlRatingHistoryRequest(BaseModel):
    """Request model for SiteExplorerUrlRatingHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY)
    date_to: DateStr | None = Field(default=None, description="The end date of the ...")
    date_from: DateStr = Field(..., description="The start date of the historical p...")
    target: str = Field(..., description="The target of the search: a domain or a URL.")

class SiteExplorerUrlRatingHistoryData(BaseModel):
    """Individual data item for /url-rating-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    url_rating: float | None = Field(default=None, description="The strength of you...")

class SiteExplorerUrlRatingHistoryResponse(BaseModel):
    """Response model for /url-rating-history endpoint"""

    url_ratings: list[SiteExplorerUrlRatingHistoryData] | None = Field(default=None)

    @property
    def data(self) -> list[SiteExplorerUrlRatingHistoryData]:
        """Unwrap the response payload."""
        return self.url_ratings or []

