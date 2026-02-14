# AUTO-GENERATED -- DO NOT EDIT

# ruff: noqa: E501, F405

from __future__ import annotations

from typing import TypeVar

from pydantic import BaseModel

from ahrefs.types._coercions import DateStr, SelectStr  # noqa: F401
from ahrefs.types._generated import *  # noqa: F401,F403

T = TypeVar('T', bound=BaseModel)


class GeneratedMethodsMixin:
    """Async endpoint methods. Mixed into AsyncAhrefsClient."""

    async def _request(
        self, api_section: str, endpoint: str, request_model: BaseModel,
        response_model_class: type[T], *, exclude_none: bool = False,
    ) -> T:
        raise NotImplementedError

    # fmt: off
    # Brand Radar API methods
    async def brand_radar_ai_responses(
        self,
        request: BrandRadarAiResponsesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        date: DateStr | None = None,
        country: CountryEnum | None = None,
        order_by: OrderByEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarAiResponsesResponse:
        """
        AI Responses.

        Args:
            request: BrandRadarAiResponsesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date (str, optional): The date to search for in YYYY-MM-DD format. Default: None.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                order_by (OrderByEnum, optional): The order by field. Default: 'relevance'.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. Default: '[]'.

        Returns:
            BrandRadarAiResponsesResponse containing BrandRadarAiResponsesData:
                country (str): The country of the question.
                links (list[dict[str, Any] | None]): (10 units) The links used for the response.
                question (str): The question asked by the user.
                response (str): (10 units) The response from the model.
                volume (int): (10 units) Estimated monthly searches. This is based on our estimates for Google, combining the search volumes of related keywords where this question appears in People Also Ask section.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarAiResponsesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("where", where), ("select", select), ("date", date), ("country", country), ("order_by", order_by), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("brand-radar", "ai-responses", request, BrandRadarAiResponsesResponse, exclude_none=True)

    async def brand_radar_impressions_history(
        self,
        request: BrandRadarImpressionsHistoryRequest | None = None,
        *,
        where: str | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarImpressionsHistoryResponse:
        """
        Overview history - Impressions.

        Args:
            request: BrandRadarImpressionsHistoryRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brand. Default: '[]'.
                brand (str, required): The brand to search for.

        Returns:
            BrandRadarImpressionsHistoryResponse containing BrandRadarImpressionsHistoryData:
                date (str): date
                impressions (int): impressions
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("data_source", data_source), ("brand", brand)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarImpressionsHistoryRequest(**{k: v for k, v in [("where", where), ("date_to", date_to), ("date_from", date_from), ("country", country), ("data_source", data_source), ("market", market), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("brand-radar", "impressions-history", request, BrandRadarImpressionsHistoryResponse, exclude_none=True)

    async def brand_radar_impressions_overview(
        self,
        request: BrandRadarImpressionsOverviewRequest | None = None,
        *,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarImpressionsOverviewResponse:
        """
        Overview - Impressions.

        Args:
            request: BrandRadarImpressionsOverviewRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand or competitors should not be empty. Default: '[]'.

        Returns:
            BrandRadarImpressionsOverviewResponse containing BrandRadarImpressionsOverviewData:
                brand (str): Brand name (either your brand or a competitor provided in the request).
                no_tracked_brands (int): Estimated impressions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified).
                only_competitors_brands (int): Estimated impressions from responses mentioning only competitor brands.
                only_target_brand (int): Estimated impressions from responses mentioning only your brand.
                target_and_competitors_brands (int): Estimated impressions from responses mentioning both your and competitor brands.
                total (int): Total estimated impressions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`).
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarImpressionsOverviewRequest(**{k: v for k, v in [("where", where), ("select", select), ("country", country), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("brand-radar", "impressions-overview", request, BrandRadarImpressionsOverviewResponse, exclude_none=True)

    async def brand_radar_mentions_history(
        self,
        request: BrandRadarMentionsHistoryRequest | None = None,
        *,
        where: str | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarMentionsHistoryResponse:
        """
        Overview history - Mentions.

        Args:
            request: BrandRadarMentionsHistoryRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brand. Default: '[]'.
                brand (str, required): The brand to search for.

        Returns:
            BrandRadarMentionsHistoryResponse containing BrandRadarMentionsHistoryData:
                date (str): date
                mentions (int): mentions
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("data_source", data_source), ("brand", brand)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarMentionsHistoryRequest(**{k: v for k, v in [("where", where), ("date_to", date_to), ("date_from", date_from), ("country", country), ("data_source", data_source), ("market", market), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("brand-radar", "mentions-history", request, BrandRadarMentionsHistoryResponse, exclude_none=True)

    async def brand_radar_mentions_overview(
        self,
        request: BrandRadarMentionsOverviewRequest | None = None,
        *,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarMentionsOverviewResponse:
        """
        Overview - Mentions.

        Args:
            request: BrandRadarMentionsOverviewRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand or competitors should not be empty. Default: '[]'.

        Returns:
            BrandRadarMentionsOverviewResponse containing BrandRadarMentionsOverviewData:
                brand (str): Brand name (either your brand or a competitor provided in the request).
                no_tracked_brands (int): Estimated mentions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified).
                only_competitors_brands (int): Estimated mentions from responses mentioning only competitor brands.
                only_target_brand (int): Estimated mentions from responses mentioning only your brand.
                target_and_competitors_brands (int): Estimated mentions from responses mentioning both your and competitor brands.
                total (int): Total estimated mentions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`).
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarMentionsOverviewRequest(**{k: v for k, v in [("where", where), ("select", select), ("country", country), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("brand-radar", "mentions-overview", request, BrandRadarMentionsOverviewResponse, exclude_none=True)

    async def brand_radar_sov_overview(
        self,
        request: BrandRadarSovOverviewRequest | None = None,
        *,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarSovOverviewResponse:
        """
        Overview - Share of Voice.

        Args:
            request: BrandRadarSovOverviewRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand or competitors should not be empty. Default: '[]'.

        Returns:
            BrandRadarSovOverviewResponse containing BrandRadarSovOverviewData:
                brand (str): Brand name (either your brand or a competitor provided in the request).
                share_of_voice (float): Estimated share of voice for your brand.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarSovOverviewRequest(**{k: v for k, v in [("where", where), ("select", select), ("country", country), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("brand-radar", "sov-overview", request, BrandRadarSovOverviewResponse, exclude_none=True)

    # Keywords Explorer API methods
    async def keywords_explorer_matching_terms(
        self,
        request: KeywordsExplorerMatchingTermsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        search_engine: SearchEngineEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
        match_mode: MatchModeEnum | None = None,
        terms: TermsEnum | None = None,
    ) -> KeywordsExplorerMatchingTermsResponse:
        """
        Matching terms.

        Args:
            request: KeywordsExplorerMatchingTermsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.
                match_mode (MatchModeEnum, optional): Keyword ideas contain the words from your query in any order (terms mode) or in the exact order they are written (phrase mode). Default: 'terms'.
                terms (TermsEnum, optional): All keywords ideas or keywords ideas phrased as questions. Default: 'all'.

        Returns:
            KeywordsExplorerMatchingTermsResponse containing KeywordsExplorerMatchingTermsData:
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerMatchingTermsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("country", country), ("search_engine", search_engine), ("keywords", keywords), ("keyword_list_id", keyword_list_id), ("match_mode", match_mode), ("terms", terms)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("keywords-explorer", "matching-terms", request, KeywordsExplorerMatchingTermsResponse, exclude_none=True)

    async def keywords_explorer_overview(
        self,
        request: KeywordsExplorerOverviewRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        volume_monthly_date_to: DateStr | None = None,
        volume_monthly_date_from: DateStr | None = None,
        target_mode: ModeEnum | None = None,
        target: str | None = None,
        target_position: TargetPositionEnum | None = None,
        country: CountryEnum | None = None,
        search_engine: SearchEngineEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
    ) -> KeywordsExplorerOverviewResponse:
        """
        Overview.

        The `regex` filter has limited functionality when used in this request, and the syntax differs from other requests. It expects an asterisk (*) symbol as a wildcard.

        Args:
            request: KeywordsExplorerOverviewRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                volume_monthly_date_to (str, optional): The end date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested. Default: None.
                volume_monthly_date_from (str, optional): The start date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested. Default: None.
                target_mode (ModeEnum, optional): The scope of the target URL you specified. Default: None.
                target (str, optional): The target of the search: a domain or a URL. Default: None.
                target_position (TargetPositionEnum, optional): Filters keywords based on the ranking position of the specified `target`. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.

        Returns:
            KeywordsExplorerOverviewResponse containing KeywordsExplorerOverviewData:
                clicks (int | None): The average monthly number of clicks on the search results that people make while searching for the target keyword.
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                parent_volume (int | None): (10 units) The search volume of the parent topic.
                searches_pct_clicks_organic_and_paid (float | None): The average monthly percentage of people who clicked on both organic and paid results while searching for the target keyword.
                searches_pct_clicks_organic_only (float | None): The average monthly percentage of people who clicked only on organic results while searching for the target keyword.
                searches_pct_clicks_paid_only (float | None): The average monthly percentage of people who clicked only on paid results while searching for the target keyword.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
                volume_monthly_history (list[dict[str, Any] | None]): (2 units per historical month, with a minimum of 50 units) Historical monthly search volume estimates of a keyword for the period set by the `volume_monthly_date_from` and `volume_monthly_date_to` parameters.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerOverviewRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("volume_monthly_date_to", volume_monthly_date_to), ("volume_monthly_date_from", volume_monthly_date_from), ("target_mode", target_mode), ("target", target), ("target_position", target_position), ("country", country), ("search_engine", search_engine), ("keywords", keywords), ("keyword_list_id", keyword_list_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("keywords-explorer", "overview", request, KeywordsExplorerOverviewResponse, exclude_none=True)

    async def keywords_explorer_related_terms(
        self,
        request: KeywordsExplorerRelatedTermsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
        view_for: ViewForEnum | None = None,
        terms: TermsEnum1 | None = None,
    ) -> KeywordsExplorerRelatedTermsResponse:
        """
        Related terms.

        Args:
            request: KeywordsExplorerRelatedTermsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.
                view_for (ViewForEnum, optional): View keywords for the top 10 or top 100 ranking pages. Default: 'top_10'.
                terms (TermsEnum1, optional): Related keywords which top-ranking pages also rank for (`also_rank_for`), additional keywords frequently mentioned in top-ranking pages (`also_talk_about`), or combination of both (`all`). Default: 'all'.

        Returns:
            KeywordsExplorerRelatedTermsResponse containing KeywordsExplorerRelatedTermsData:
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerRelatedTermsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("country", country), ("keywords", keywords), ("keyword_list_id", keyword_list_id), ("view_for", view_for), ("terms", terms)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("keywords-explorer", "related-terms", request, KeywordsExplorerRelatedTermsResponse, exclude_none=True)

    async def keywords_explorer_search_suggestions(
        self,
        request: KeywordsExplorerSearchSuggestionsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        search_engine: SearchEngineEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
    ) -> KeywordsExplorerSearchSuggestionsResponse:
        """
        Search suggestions.

        Args:
            request: KeywordsExplorerSearchSuggestionsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.

        Returns:
            KeywordsExplorerSearchSuggestionsResponse containing KeywordsExplorerSearchSuggestionsData:
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerSearchSuggestionsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("country", country), ("search_engine", search_engine), ("keywords", keywords), ("keyword_list_id", keyword_list_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("keywords-explorer", "search-suggestions", request, KeywordsExplorerSearchSuggestionsResponse, exclude_none=True)

    async def keywords_explorer_volume_by_country(
        self,
        request: KeywordsExplorerVolumeByCountryRequest | None = None,
        *,
        limit: int | None = None,
        search_engine: SearchEngineEnum | None = None,
        keyword: str | None = None,
    ) -> KeywordsExplorerVolumeByCountryResponse:
        """
        Volume by country.

        Args:
            request: KeywordsExplorerVolumeByCountryRequest
                limit (int, optional): The number of results to return. Default: None.
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keyword (str, required): The keyword to show metrics for.

        Returns:
            KeywordsExplorerVolumeByCountryResponse containing KeywordsExplorerVolumeByCountryData:
                country (str)
                volume (int): (10 units) An estimation of the average monthly number of searches for a keyword in a given country.
        """
        if request is None:
            _missing = [k for k, v in [("keyword", keyword)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerVolumeByCountryRequest(**{k: v for k, v in [("limit", limit), ("search_engine", search_engine), ("keyword", keyword)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("keywords-explorer", "volume-by-country", request, KeywordsExplorerVolumeByCountryResponse, exclude_none=True)

    async def keywords_explorer_volume_history(
        self,
        request: KeywordsExplorerVolumeHistoryRequest | None = None,
        *,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        keyword: str | None = None,
    ) -> KeywordsExplorerVolumeHistoryResponse:
        """
        Volume history.

        Args:
            request: KeywordsExplorerVolumeHistoryRequest
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, optional): The start date of the historical period in YYYY-MM-DD format. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                keyword (str, required): The keyword to show metrics for.

        Returns:
            KeywordsExplorerVolumeHistoryResponse containing KeywordsExplorerVolumeHistoryData:
                date (str)
                volume (int): An estimation of the number of searches for a keyword over a given month.
        """
        if request is None:
            _missing = [k for k, v in [("country", country), ("keyword", keyword)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerVolumeHistoryRequest(**{k: v for k, v in [("date_to", date_to), ("date_from", date_from), ("country", country), ("keyword", keyword)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("keywords-explorer", "volume-history", request, KeywordsExplorerVolumeHistoryResponse, exclude_none=True)

    # Rank Tracker API methods
    async def rank_tracker_competitors_overview(
        self,
        request: RankTrackerCompetitorsOverviewRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerCompetitorsOverviewResponse:
        """
        Competitors overview.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerCompetitorsOverviewRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerCompetitorsOverviewResponse containing RankTrackerCompetitorsOverviewData:
                competitors_list (list[dict[str, Any] | None]): Competitors information for a given keyword. The following fields are included: `url`, `url_prev`, `position`, `position_prev`, `best_position_kind`, `best_position_kind`, `traffic`, `traffic_prev`, `value`, `value_prev`. Fields ending in `prev` are included only in the compared view.
                country (CountryEnum1): The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2).
                keyword (str): The keyword your target ranks for.
                keyword_difficulty (int | None): An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                keyword_has_data (bool): Will return `false` if the keyword is still processing and no SERP has been fetched yet.
                keyword_is_frozen (bool): Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are "frozen", meaning they do not have their rankings updated.
                language (str): The SERP language that a given keyword is being tracked for.
                location (str): The location (country, state/province, or city) that a given keyword is being tracked in.
                serp_features (list[SerpFeaturesItemEnum1 | None]): The SERP features that appear in search results for a keyword.
                serp_updated (str | None): The date when we last checked search engine results for a keyword.
                serp_updated_prev (str | None): The date when we checked search engine results up to the comparison date.
                tags (list[str | None]): A list of tags assigned to a given keyword.
                volume (int | None): An estimation of the average monthly number of searches for a keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerCompetitorsOverviewRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("date_compared", date_compared), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("rank-tracker", "competitors-overview", request, RankTrackerCompetitorsOverviewResponse, exclude_none=True)

    async def rank_tracker_competitors_pages(
        self,
        request: RankTrackerCompetitorsPagesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        target_and_tracked_competitors_only: bool | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerCompetitorsPagesResponse:
        """
        Competitors pages.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerCompetitorsPagesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                target_and_tracked_competitors_only (bool, optional): Restrict pages to target and tracked competitors Default: False.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerCompetitorsPagesResponse containing RankTrackerCompetitorsPagesData:
                keywords (int): The total number of keywords that your target ranks for in the top 100 organic search results.
                share_of_traffic_value (float): The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords.
                share_of_traffic_value_prev (float): The share of traffic value on the comparison date.
                share_of_voice (float): The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords.
                share_of_voice_prev (float): The share of voice on the comparison date.
                status (StatusEnum): The status of a page: the new page that just started to rank ("left"), the lost page that disappeared from search results ("right"), or no change ("both").
                title (str | None): The title displayed for the page in its top keyword's SERP.
                title_prev (str | None): The title on the comparison date.
                traffic (int): An estimation of the number of monthly visits that a page gets from organic search.
                traffic_prev (int): The traffic on the comparison date.
                traffic_value (int | None): The estimated value of a page’s monthly organic search traffic, in USD cents.
                traffic_value_prev (int | None): The traffic value on the comparison date.
                url (str): The page URL.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerCompetitorsPagesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("target_and_tracked_competitors_only", target_and_tracked_competitors_only), ("date_compared", date_compared), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("rank-tracker", "competitors-pages", request, RankTrackerCompetitorsPagesResponse, exclude_none=True)

    async def rank_tracker_competitors_stats(
        self,
        request: RankTrackerCompetitorsStatsRequest | None = None,
        *,
        select: SelectStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerCompetitorsStatsResponse:
        """
        Competitors metrics.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerCompetitorsStatsRequest
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerCompetitorsStatsResponse containing RankTrackerCompetitorsStatsData:
                ai_overview_count (int): The total number of tracked keywords for which your target ranks in an AI Overview.
                average_position (float | None): The average of your target's top organic positions across all tracked keywords.
                competitor (str): Competitor's URL.
                discussions_count (int): The total number of tracked keywords for which your target ranks in Discussions and forums.
                featured_snippet_count (int): The total number of tracked keywords for which your target ranks in a Featured snippet.
                image_pack_count (int): The total number of tracked keywords for which your target ranks in an Image pack.
                knowledge_card_count (int): The total number of tracked keywords for which your target ranks in a Knowledge card.
                knowledge_panel_count (int): The total number of tracked keywords for which your target ranks in a Knowledge panel.
                pos_11_20 (int): The total number of tracked keywords for which your target's top organic position is within the 11th to 20th results.
                pos_1_3 (int): The total number of tracked keywords for which your target's top organic position is within the top 3 results.
                pos_21_50 (int): The total number of tracked keywords for which your target's top organic position is within the 21st to 50th results.
                pos_4_10 (int): The total number of tracked keywords for which your target's top organic position is within the 4th to 10th results.
                pos_51_plus (int): The total number of tracked keywords for which your target's top organic position is the 51st or higher.
                pos_no_rank (int): The total number of tracked keywords where your target doesn't rank.
                share_of_traffic_value (float): The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords.
                share_of_voice (float): The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords.
                sitelinks_count (int): The total number of tracked keywords for which your target ranks in Sitelinks.
                thumbnail_count (int): The total number of tracked keywords for which your target ranks in a Thumbnail.
                top_stories_count (int): The total number of tracked keywords for which your target ranks in Top stories.
                traffic (int | None): The estimated number of monthly visits that your target gets from organic search for all tracked keywords.
                traffic_value (int | None): The estimated value of your target's monthly organic search traffic for all tracked keywords.
                video_preview_count (int): The total number of tracked keywords for which your target ranks in a Video preview.
                videos_count (int): The total number of tracked keywords for which your target ranks in Videos.
                x_count (int): The total number of tracked keywords for which your target ranks in an X (Twitter) widget.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerCompetitorsStatsRequest(**{k: v for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("rank-tracker", "competitors-stats", request, RankTrackerCompetitorsStatsResponse, exclude_none=True)

    async def rank_tracker_overview(
        self,
        request: RankTrackerOverviewRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerOverviewResponse:
        """
        Overview.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerOverviewRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerOverviewResponse containing RankTrackerOverviewData:
                best_position_has_thumbnail (bool | None): The top position (or target URL’s, if set) has a thumbnail.
                best_position_has_thumbnail_previous (bool | None): The top position (or target URL’s, if set) has a thumbnail on the comparison date.
                best_position_has_video_preview (bool | None): The top position (or target URL’s, if set) has a video preview.
                best_position_has_video_preview_previous (bool | None): The top position (or target URL’s, if set) has a video preview on the comparison date.
                best_position_kind (BestPositionKindEnum | None): The kind of top position (or target URL’s, if set): organic, paid, or a SERP feature.
                best_position_kind_previous (BestPositionKindEnum | None): The kind of top position (or target URL’s, if set) on the comparison date.
                clicks (int | None): Clicks metric refers to the average monthly number of clicks on the search results that people make while searching for the target keyword. Some searches generate clicks on multiple results, while others might not end in any clicks at all.
                clicks_per_search (float | None): Clicks Per Search is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                cost_per_click (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword.
                country (CountryEnum1): The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2).
                country_prev (CountryEnum1): The country that a given keyword is being tracked in on the comparison date. A two-letter country code (ISO 3166-1 alpha-2).
                created_at (str): The date when a keyword was added to the project.
                is_branded (bool): User intent: branded. The user is searching for a specific brand or company name.
                is_commercial (bool): User intent: commercial. The user is comparing products or services before making a purchase decision.
                is_informational (bool): User intent: informational. The user is looking for information or an answer to a specific question.
                is_local (bool): User intent: local. The user is looking for information relevant to a specific location or nearby services.
                is_navigational (bool): User intent: navigational. The user is searching for a specific website or web page.
                is_transactional (bool): User intent: transactional. The user is ready to complete an action, often a purchase.
                keyword (str): The keyword your target ranks for.
                keyword_difficulty (int | None): An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                keyword_has_data (bool): Will return `false` if the keyword is still processing and no SERP has been fetched yet.
                keyword_is_frozen (bool): Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are "frozen", meaning they do not have their rankings updated.
                keyword_prev (str): The keyword your target ranks for on the comparison date.
                language (str): The SERP language that a given keyword is being tracked for.
                language_prev (str): The SERP language on the comparison date.
                location (str): The location (country, state/province, or city) that a given keyword is being tracked in.
                location_prev (str): The location (country, state/province, or city) that a given keyword is being tracked in on the comparison date.
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead.  To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                position (int | None): The top position (or target URL’s, if set) in organic search.
                position_diff (int | None): The change in top position (or target URL’s, if set) between selected dates.
                ... and 20 more fields. See RankTrackerOverviewData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerOverviewRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("date_compared", date_compared), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("rank-tracker", "overview", request, RankTrackerOverviewResponse, exclude_none=True)

    async def rank_tracker_serp_overview(
        self,
        request: RankTrackerSerpOverviewRequest | None = None,
        *,
        top_positions: int | None = None,
        device: DeviceEnum | None = None,
        date: str | None = None,
        location_id: int | None = None,
        country: CountryEnum | None = None,
        language_code: str | None = None,
        keyword: str | None = None,
        project_id: int | None = None,
    ) -> RankTrackerSerpOverviewResponse:
        """
        SERP Overview.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerSerpOverviewRequest
                top_positions (int, optional): The number of top organic SERP positions to return. If not specified, all available positions will be returned. Default: None.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                date (str, optional): A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned. Default: None.
                location_id (int, optional): The location ID of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                language_code (str, optional): The language code of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords. Default: None.
                keyword (str, required): The keyword to return SERP Overview for.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`

        Returns:
            RankTrackerSerpOverviewResponse containing RankTrackerSerpOverviewData:
                position (int): The position of the search result in SERP.
                title (str | None): The title of a ranking page.
                url (str | None): The URL of a ranking page.
                type (list[str | None]): The kind of the position: organic, paid, or a SERP feature. Allowed values: `ai_overview`, `ai_overview_sitelink`, `discussion`, `image`, `image_th`, `knowledge_card`, `knowledge_panel`, `local_pack`, `organic`, `organic_shopping`, `paid_top`, `paid_bottom`, `paid_right`, `question`, `sitelink`, `snippet`, `top_story`, `tweet`, `video`, `video_th`.
                update_date (str): The date when we checked search engine results for a keyword.
                nr_words (int | None): The total number of words present in the HTML of a web page.
                domain_rating (float | None): The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale.
                url_rating (float | None): The strength of a page's backlink profile on a 100-point logarithmic scale.
                ahrefs_rank (int | None): The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                backlinks (int | None): The total number of links from other websites pointing to a search result.
                refdomains (int | None): The total number of unique domains linking to a search result.
                traffic (int | None): An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for.
                value (int | None): The estimated value of a page’s monthly organic search traffic, in USD cents.
                keywords (int | None): The total number of keywords that a search result ranks for in the top 100 organic positions.
                top_keyword (str | None): The keyword that brings the most organic traffic to a search result.
                top_keyword_volume (int | None): An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data.
        """
        if request is None:
            _missing = [k for k, v in [("device", device), ("country", country), ("keyword", keyword), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerSerpOverviewRequest(**{k: v for k, v in [("top_positions", top_positions), ("device", device), ("date", date), ("location_id", location_id), ("country", country), ("language_code", language_code), ("keyword", keyword), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("rank-tracker", "serp-overview", request, RankTrackerSerpOverviewResponse, exclude_none=True)

    # Serp Overview API methods
    async def serp_overview_serp_overview(
        self,
        request: SerpOverviewSerpOverviewRequest | None = None,
        *,
        select: SelectStr | None = None,
        top_positions: int | None = None,
        date: str | None = None,
        country: CountryEnum | None = None,
        keyword: str | None = None,
    ) -> SerpOverviewSerpOverviewResponse:
        """
        SERP Overview.

        Args:
            request: SerpOverviewSerpOverviewRequest
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                top_positions (int, optional): The number of top organic SERP positions to return. If not specified, all available positions will be returned. Default: None.
                date (str, optional): A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                keyword (str, required): The keyword to return SERP Overview for.

        Returns:
            SerpOverviewSerpOverviewResponse containing SerpOverviewSerpOverviewData:
                ahrefs_rank (int | None): The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                backlinks (int | None): The total number of links from other websites pointing to a search result.
                domain_rating (float | None): The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale.
                keywords (int | None): The total number of keywords that a search result ranks for in the top 100 organic positions.
                position (int): The position of the search result in SERP.
                refdomains (int | None): (5 units) The total number of unique domains linking to a search result.
                title (str | None): The title of a ranking page.
                top_keyword (str | None): The keyword that brings the most organic traffic to a search result.
                top_keyword_volume (int | None): (10 units) An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data.
                traffic (int | None): (10 units) An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for.
                type (list[SerpFeaturesItemEnum1 | None]): The kind of the position: organic, paid, or a SERP feature.
                update_date (str): The date when we checked search engine results for a keyword.
                url (str | None): The URL of a ranking page.
                url_rating (float | None): The strength of a page's backlink profile on a 100-point logarithmic scale.
                value (int | None): (10 units) The estimated value of a page’s monthly organic search traffic, in USD cents.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country), ("keyword", keyword)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SerpOverviewSerpOverviewRequest(**{k: v for k, v in [("select", select), ("top_positions", top_positions), ("date", date), ("country", country), ("keyword", keyword)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("serp-overview", "serp-overview", request, SerpOverviewSerpOverviewResponse, exclude_none=True)

    # Site Audit API methods
    async def site_audit_issues(
        self,
        request: SiteAuditIssuesRequest | None = None,
        *,
        date_compared: str | None = None,
        date: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditIssuesResponse:
        """
        Project Issues.

        >This endpoint consumes a fixed cost of 50 API units per request.

        Args:
            request: SiteAuditIssuesRequest
                date_compared (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field. Default: None.
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`

        Returns:
            SiteAuditIssuesResponse containing SiteAuditIssuesData:
                issue_id (str): The unique identifier of the issue.
                name (str): The name of the issue.
                importance (str): The importance of the issue. Possible values: `Error`, `Warning`, `Notice`.
                category (str): The category of the issue. Possible values: `Internal pages`, `Indexability`, `Links`, `Redirects`, `Content`, `Social tags`, `Duplicates`, `Localization`, `Usability and performance`, `Images`, `JavaScript`, `CSS`, `Sitemaps`, `External pages`, `Other`.
                is_indexable (bool | None): True if the issue applies only to indexable pages.
                crawled (int): Number of URLs currently affected by the issue.
                change (int | None): Difference in the number of affected URLs between the specified dates.
                added (int | None): Number of URLs that have the issue on the current date but did not have it on the previous date.
                new (int | None): Number of newly discovered URLs that have the issue on the current date.
                removed (int | None): Number of URLs that had the issue on the previous date but no longer have it on the current date.
                missing (int | None): Number of URLs that had the issue on the previous date but cannot be found on the current date.
        """
        if request is None:
            _missing = [k for k, v in [("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteAuditIssuesRequest(**{k: v for k, v in [("date_compared", date_compared), ("date", date), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-audit", "issues", request, SiteAuditIssuesResponse, exclude_none=True)

    async def site_audit_page_content(
        self,
        request: SiteAuditPageContentRequest | None = None,
        *,
        select: SelectStr | None = None,
        date: str | None = None,
        target_url: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditPageContentResponse:
        """
        Page content.

        >This endpoint consumes a fixed cost of 50 API units per request.

        Args:
            request: SiteAuditPageContentRequest
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                target_url (str, required): The URL of the page to retrieve content for.
                project_id (int, required): The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`

        Returns:
            SiteAuditPageContentResponse containing SiteAuditPageContentData:
                crawl_datetime (str): The timestamp when the page was crawled.
                page_text (str | None): The text extracted from the page content.
                raw_html (str | None): The raw HTML of the page.
                rendered_html (str | None): The rendered HTML of the page.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target_url", target_url), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteAuditPageContentRequest(**{k: v for k, v in [("select", select), ("date", date), ("target_url", target_url), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-audit", "page-content", request, SiteAuditPageContentResponse, exclude_none=True)

    async def site_audit_page_explorer(
        self,
        request: SiteAuditPageExplorerRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        filter_mode: FilterModeEnum | None = None,
        issue_id: str | None = None,
        date_compared: str | None = None,
        date: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditPageExplorerResponse:
        """
        Page explorer.

        >This endpoint consumes a fixed cost of 50 API units per request.

        Args:
            request: SiteAuditPageExplorerRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'page_rating,url,is_rendered,http_code,content_type,title,meta_description,h1,traffic,canonical,canonical_code,redirect,redirect_code,compliant,page_is_noindex,page_is_nofollow,incoming_all_links,links_count_internal,links_count_external,links_count_internal4xx,links_count_external4xx,hreflang_issues,psi_crux_cls_category,psi_crux_lcp_category,psi_crux_inp_category,jsonld_schema_types,jsonld_validation_kinds,origin,depth'.
                filter_mode (FilterModeEnum, optional): Indicates which pages to return compared to the previous crawl. If not specified, all URLs that match your filter conditions are returned. `added`: URLs that are a new match for your filter conditions. `new`: URLs that are newly crawled and match your filter conditions. `removed`: URLs that stopped matching your filter conditions. `missing`: URLs that weren't crawled, but previously matched your filter conditions. `no_change`: URLs that match your filter conditions in a crawl and the crawl before it. Default: None.
                issue_id (str, optional): The unique identifier of an issue. When specified, only URLs affected by this issue are returned. You can get issue IDs by querying the `site-audit/issues` endpoint. Default: None.
                date_compared (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field. Default: None.
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                project_id (int, required): The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`

        Returns:
            SiteAuditPageExplorerResponse containing SiteAuditPageExplorerData:
                ai_content_level (str | None): The estimated percentage of AI-generated text on the page. Possible values: `None`, `Low`, `Moderate`, `High`, `Very High`
                ai_content_status (str | None): AI detection status for each page. Possible values: - `Success`: Content analyzed successfully - `Content_too_short`: Not enough text for reliable detection - `Not_eligible`: URL isn't an internal HTML page - `Failed`: Internal issue prevented detection - `Detection_off`: Disabled in Crawl settings
                alternate (int | None): The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database)
                alternate_diff (int | None): The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database)
                alternate_prev (int | None): The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database)
                backlinks (int | None): The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                backlinks_diff (int | None): The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                backlinks_prev (int | None): The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical (str | None): The URL of the canonical version of the page
                canonical_code (int | None): The HTTP status code of the canonical URL
                canonical_counts (int | None): The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical_counts_diff (int | None): The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical_counts_prev (int | None): The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical_group_hash (int | None): The ID of the group of pages that have the same canonical URL
                canonical_is_canonical (bool | None): Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical
                canonical_is_canonical_prev (bool | None): Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical
                canonical_no_crawl_reason (str | None): The reason why the canonical version of the page was not crawled
                canonical_no_crawl_reason_prev (str | None): The reason why the canonical version of the page was not crawled
                canonical_prev (str | None): The URL of the canonical version of the page
                canonical_scheme (str | None): The protocol of the canonical URL
                canonical_scheme_prev (str | None): The protocol of the canonical URL
                compliant (bool | None): Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the "rel=canonical" tag pointing to a different URL nor the "noindex" directive
                compliant_prev (bool | None): Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the "rel=canonical" tag pointing to a different URL nor the "noindex" directive
                compression (str | None): The data compression scheme
                compression_prev (str | None): The data compression scheme
                content_encoding (str | None): The Content-Encoding HTTP response header field
                content_encoding_prev (str | None): The Content-Encoding HTTP response header field
                content_length (int | None): The character length of content displayed on the page
                content_length_diff (int | None): The character length of content displayed on the page
                content_length_prev (int | None): The character length of content displayed on the page
                ... and 575 more fields. See SiteAuditPageExplorerData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteAuditPageExplorerRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("filter_mode", filter_mode), ("issue_id", issue_id), ("date_compared", date_compared), ("date", date), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-audit", "page-explorer", request, SiteAuditPageExplorerResponse, exclude_none=True)

    async def site_audit_projects(
        self,
        request: SiteAuditProjectsRequest | None = None,
        *,
        date: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditProjectsResponse:
        """
        Project Health Scores.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: SiteAuditProjectsRequest
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                project_id (int, optional): The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#` Default: None.

        Returns:
            SiteAuditProjectsResponse containing SiteAuditProjectsData:
                project_id (str): The unique identifier of the project.
                project_name (str): The project name.
                target_protocol (str): The protocol of the target. Possible values: `both`, `http`, `https`.
                target_url (str): The URL of the project's target.
                target_mode (str): The scope of the target. Possible values: `exact`, `prefix`, `domain`, `subdomains`.
                date (str | None): The finish date and time of the last finished crawl, in GMT time zone.
                status (str | None): The status of the most recent finished crawl. Possible values: `Completed`, `Stopped`, `Error`, `In_progress`.
                health_score (int | None): Reflects the proportion of internal URLs on your site that do not have errors, based on the last finished crawl. Excludes crawls that are starting, in progress, finalizing, or were skipped.
                urls_with_errors (int | None): Number of internal URLs with errors
                urls_with_warnings (int | None): Number of internal URLs with warnings
                urls_with_notices (int | None): Number of internal URLs with notices
                total (int | None): Number of total crawled internal URLs
        """
        if request is None:
            request = SiteAuditProjectsRequest(**{k: v for k, v in [("date", date), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-audit", "projects", request, SiteAuditProjectsResponse, exclude_none=True)

    # Site Explorer API methods
    async def site_explorer_all_backlinks(
        self,
        request: SiteExplorerAllBacklinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        aggregation: AggregationEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerAllBacklinksResponse:
        """
        Backlinks.

        Args:
            request: SiteExplorerAllBacklinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `link_group_count`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                aggregation (AggregationEnum, optional): The backlinks grouping mode. Default: 'similar_links'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerAllBacklinksResponse containing SiteExplorerAllBacklinksData:
                ahrefs_rank_source (int): The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                ahrefs_rank_target (int): The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                alt (str | None): The alt attribute of the link.
                anchor (str): The clickable words in a link that point to a URL.
                broken_redirect_new_target (str | None): The new destination of a modified redirect.
                broken_redirect_reason (BrokenRedirectReasonEnum | None): The reason the redirect was considered broken during the last crawl.
                broken_redirect_source (str | None): The redirecting URL that was modified, causing the redirect to become broken.
                class_c (int): (5 units) The number of unique class_c subnets linking to the referring page.
                discovered_status (DiscoveredStatusEnum | None): The reason the link was discovered during the last crawl: the page was crawled for the first time, the link was added to the page, or the link re-appeared after being removed.
                domain_rating_source (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                domain_rating_target (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                drop_reason (DropReasonEnum | None): The reason we removed the link from our index.
                encoding (str): The character set encoding of the referring page HTML.
                first_seen (str): The date the referring page URL was first discovered.
                first_seen_link (str): The date we first found a backlink to your target on a given referring page.
                http_code (int): The return code from HTTP protocol returned during the referring page crawl.
                http_crawl (bool): The link was discovered without executing javascript and rendering the page.
                ip_source (str | None): The referring domain IP address.
                is_alternate (bool): The link with the rel=“alternate” attribute.
                is_canonical (bool): The link with the rel=“canonical” attribute.
                is_content (bool): The link was found in the biggest piece of content on the page.
                is_dofollow (bool): The link has no special nofollow attribute.
                is_form (bool): The link was found in a form HTML tag.
                is_frame (bool): The link was found in an iframe HTML tag.
                is_image (bool): The link is a regular link that has an image inside their href attribute.
                is_lost (bool): The link currently does not exist anymore.
                is_new (bool): The link was discovered on the last crawl.
                is_nofollow (bool): The link or the referring page has the nofollow attribute set.
                is_redirect (bool): The link pointing to your target via a redirect.
                is_redirect_lost (bool): The redirected link currently does not exist anymore.
                ... and 50 more fields. See SiteExplorerAllBacklinksData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerAllBacklinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("aggregation", aggregation), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "all-backlinks", request, SiteExplorerAllBacklinksResponse, exclude_none=True)

    async def site_explorer_anchors(
        self,
        request: SiteExplorerAnchorsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerAnchorsResponse:
        """
        Anchors.

        Args:
            request: SiteExplorerAnchorsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerAnchorsResponse containing SiteExplorerAnchorsData:
                anchor (str): The clickable words in a link that point to a URL.
                dofollow_links (int): The number of links with a given anchor to your target that don’t have the “nofollow” attribute.
                first_seen (str): The date we first found a link with a given anchor to your target.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                last_seen (str | None): The date we discovered the last backlink with a given anchor was lost.
                links_to_target (int): The number of inbound backlinks your target has with a given anchor.
                lost_links (int): The number of backlinks with a given anchor lost during the selected time period.
                new_links (int): The number of new backlinks with a given anchor found during the selected time period.
                refdomains (int): (5 units) The number of unique domains linking to your target with a given anchor.
                refpages (int): The number of pages containing a link with a given anchor to your target.
                top_domain_rating (float): The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerAnchorsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "anchors", request, SiteExplorerAnchorsResponse, exclude_none=True)

    async def site_explorer_backlinks_stats(
        self,
        request: SiteExplorerBacklinksStatsRequest | None = None,
        *,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerBacklinksStatsResponse:
        """
        Backlinks stats.

        Args:
            request: SiteExplorerBacklinksStatsRequest
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerBacklinksStatsResponse containing SiteExplorerBacklinksStatsData:
                live (int): The total number of links from other websites pointing to your target.
                all_time (int): The total number of links from other websites pointing to your target for all time.
                live_refdomains (int): (5 units) The total number of unique domains linking to your target.
                all_time_refdomains (int): (5 units) The total number of unique domains linking to your target for all time.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBacklinksStatsRequest(**{k: v for k, v in [("protocol", protocol), ("target", target), ("mode", mode), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "backlinks-stats", request, SiteExplorerBacklinksStatsResponse, exclude_none=True)

    async def site_explorer_best_by_external_links(
        self,
        request: SiteExplorerBestByExternalLinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerBestByExternalLinksResponse:
        """
        Best by External Links.

        Args:
            request: SiteExplorerBestByExternalLinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `http_code_target`, `languages_target`, `last_visited_target`, `powered_by_target`, `target_redirect`, `title_target`, `url_rating_target`, which are not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerBestByExternalLinksResponse containing SiteExplorerBestByExternalLinksData:
                dofollow_to_target (int): The number of links to your target page that don’t have the “nofollow” attribute.
                first_seen_link (str): The date we first found a link to your target.
                http_code_target (int | None): The return code from HTTP protocol returned during the target page crawl.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                languages_target (list[str | None]): The languages listed in the target page metadata or detected by the crawler to appear in the HTML.
                last_seen (str | None): The date your target page lost its last live link.
                last_visited_source (str): The date we last verified a live link to your target page.
                last_visited_target (str | None): The date we last crawled your target page.
                links_to_target (int): The number of inbound backlinks the target page has.
                lost_links_to_target (int): The number of backlinks lost during the selected time period.
                new_links_to_target (int): The number of new backlinks found during the selected time period.
                nofollow_to_target (int): The number of links to your target page that have the “nofollow” attribute.
                powered_by_target (list[str | None]): Web technologies used to build and serve the target page content.
                redirects_to_target (int): The number of inbound redirects to your target page.
                refdomains_target (int): (5 units) The number of unique referring domains linking to the target page.
                target_redirect (str | None): The target's redirect if any.
                title_target (str | None): The html title of the target page.
                top_domain_rating_source (float): The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.
                url_rating_target (float | None): The strength of the target page's backlink profile compared to the others in our database on a 100-point scale.
                url_to (str): The URL the backlink points to.
                url_to_plain (str): The target page URL optimized for use as a filter.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBestByExternalLinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "best-by-external-links", request, SiteExplorerBestByExternalLinksResponse, exclude_none=True)

    async def site_explorer_best_by_internal_links(
        self,
        request: SiteExplorerBestByInternalLinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerBestByInternalLinksResponse:
        """
        Best by Internal Links.

        Args:
            request: SiteExplorerBestByInternalLinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerBestByInternalLinksResponse containing SiteExplorerBestByInternalLinksData:
                canonical_to_target (int): The number of inbound canonical links to your target page.
                dofollow_to_target (int): The number of links to your target page that don’t have the “nofollow” attribute.
                first_seen_link (str): The date we first found a link to your target.
                http_code_target (int | None): The return code from HTTP protocol returned during the target page crawl.
                languages_target (list[str | None]): The languages listed in the target page metadata or detected by the crawler to appear in the HTML.
                last_seen (str | None): The date your target page lost its last live link.
                last_visited_source (str): The date we last verified a live link to your target page.
                last_visited_target (str | None): The date we last crawled your target page.
                links_to_target (int): The number of inbound backlinks the target page has.
                nofollow_to_target (int): The number of links to your target page that have the “nofollow” attribute.
                powered_by_target (list[str | None]): Web technologies used to build and serve the target page content.
                redirects_to_target (int): The number of inbound redirects to your target page.
                target_redirect (str | None): The target's redirect if any.
                title_target (str | None): The html title of the target page.
                url_rating_target (float | None): The strength of the target page's backlink profile compared to the others in our database on a 100-point scale.
                url_to (str): The URL the backlink points to.
                url_to_plain (str): The target page URL optimized for use as a filter.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBestByInternalLinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "best-by-internal-links", request, SiteExplorerBestByInternalLinksResponse, exclude_none=True)

    async def site_explorer_broken_backlinks(
        self,
        request: SiteExplorerBrokenBacklinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        aggregation: AggregationEnum | None = None,
    ) -> SiteExplorerBrokenBacklinksResponse:
        """
        Broken Backlinks.

        Args:
            request: SiteExplorerBrokenBacklinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `link_group_count`, `last_visited_target`, `http_code_target`, which are not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                aggregation (AggregationEnum, optional): The backlinks grouping mode. Default: 'similar_links'.

        Returns:
            SiteExplorerBrokenBacklinksResponse containing SiteExplorerBrokenBacklinksData:
                ahrefs_rank_source (int): The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                ahrefs_rank_target (int): The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                alt (str | None): The alt attribute of the link.
                anchor (str): The clickable words in a link that point to a URL.
                class_c (int): (5 units) The number of unique class_c subnets linking to the referring page.
                domain_rating_source (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                domain_rating_target (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                encoding (str): The character set encoding of the referring page HTML.
                first_seen (str): The date the referring page URL was first discovered.
                first_seen_link (str): The date we first found a backlink to your target on a given referring page.
                http_code (int): The return code from HTTP protocol returned during the referring page crawl.
                http_code_target (int | None): The return code from HTTP protocol returned during the target page crawl.
                http_crawl (bool): The link was discovered without executing javascript and rendering the page.
                ip_source (str | None): The referring domain IP address.
                is_alternate (bool): The link with the rel=“alternate” attribute.
                is_canonical (bool): The link with the rel=“canonical” attribute.
                is_content (bool): The link was found in the biggest piece of content on the page.
                is_dofollow (bool): The link has no special nofollow attribute.
                is_form (bool): The link was found in a form HTML tag.
                is_frame (bool): The link was found in an iframe HTML tag.
                is_image (bool): The link is a regular link that has an image inside their href attribute.
                is_nofollow (bool): The link or the referring page has the nofollow attribute set.
                is_redirect (bool): The link pointing to your target via a redirect.
                is_root_source (bool): The referring domain name is a root domain name.
                is_root_target (bool): The target domain name is a root domain name.
                is_rss (bool): The link was found in an RSS feed.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                is_sponsored (bool): The link has the Sponsored attribute set in the referring page HTML.
                is_text (bool): The link is a standard href hyperlink.
                is_ugc (bool): The link has the User Generated Content attribute set in the referring page HTML.
                ... and 41 more fields. See SiteExplorerBrokenBacklinksData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBrokenBacklinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("aggregation", aggregation)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "broken-backlinks", request, SiteExplorerBrokenBacklinksResponse, exclude_none=True)

    async def site_explorer_domain_rating(
        self,
        request: SiteExplorerDomainRatingRequest | None = None,
        *,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerDomainRatingResponse:
        """
        Domain rating.

        Args:
            request: SiteExplorerDomainRatingRequest
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerDomainRatingResponse containing SiteExplorerDomainRatingData:
                domain_rating (float): The strength of your target's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.
                ahrefs_rank (int | None): The strength of your target's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerDomainRatingRequest(**{k: v for k, v in [("protocol", protocol), ("target", target), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "domain-rating", request, SiteExplorerDomainRatingResponse, exclude_none=True)

    async def site_explorer_domain_rating_history(
        self,
        request: SiteExplorerDomainRatingHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        target: str | None = None,
    ) -> SiteExplorerDomainRatingHistoryResponse:
        """
        Domain Rating history.

        Args:
            request: SiteExplorerDomainRatingHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                target (str, required): The target of the search: a domain or a URL.

        Returns:
            SiteExplorerDomainRatingHistoryResponse containing SiteExplorerDomainRatingHistoryData:
                date (str)
                domain_rating (float): The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerDomainRatingHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("target", target)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "domain-rating-history", request, SiteExplorerDomainRatingHistoryResponse, exclude_none=True)

    async def site_explorer_keywords_history(
        self,
        request: SiteExplorerKeywordsHistoryRequest | None = None,
        *,
        select: SelectStr | None = None,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerKeywordsHistoryResponse:
        """
        Keywords history.

        Args:
            request: SiteExplorerKeywordsHistoryRequest
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'date,top3,top4_10,top11_plus'.
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerKeywordsHistoryResponse containing SiteExplorerKeywordsHistoryData:
                date (str)
                top11_20 (int): The total number of keywords that your target ranks for in the top 11-20 organic search results.
                top11_plus (int): The total number of keywords that your target ranks for in the top 11+ organic search results.
                top21_50 (int): The total number of keywords that your target ranks for in the top 21-50 organic search results.
                top3 (int): The total number of keywords that your target ranks for in the top 3 organic search results.
                top4_10 (int): The total number of keywords that your target ranks for in the top 4-10 organic search results.
                top51_plus (int): The total number of keywords that your target ranks for in the top 51+ organic search results.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerKeywordsHistoryRequest(**{k: v for k, v in [("select", select), ("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "keywords-history", request, SiteExplorerKeywordsHistoryResponse, exclude_none=True)

    async def site_explorer_linked_anchors_external(
        self,
        request: SiteExplorerLinkedAnchorsExternalRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerLinkedAnchorsExternalResponse:
        """
        Outgoing external anchors.

        Args:
            request: SiteExplorerLinkedAnchorsExternalRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerLinkedAnchorsExternalResponse containing SiteExplorerLinkedAnchorsExternalData:
                anchor (str): The clickable words in a link that point to a URL.
                dofollow_links (int): The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute.
                first_seen (str): The date we first found a link with a given anchor on your target.
                linked_domains (int): The number of unique domains linked from your target with a given anchor.
                linked_pages (int): The number of unique pages linked from your target with a given anchor.
                links_from_target (int): The number of outbound links your target has with a given anchor.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerLinkedAnchorsExternalRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "linked-anchors-external", request, SiteExplorerLinkedAnchorsExternalResponse, exclude_none=True)

    async def site_explorer_linked_anchors_internal(
        self,
        request: SiteExplorerLinkedAnchorsInternalRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerLinkedAnchorsInternalResponse:
        """
        Outgoing internal anchors.

        Args:
            request: SiteExplorerLinkedAnchorsInternalRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerLinkedAnchorsInternalResponse containing SiteExplorerLinkedAnchorsInternalData:
                anchor (str): The clickable words in a link that point to a URL.
                dofollow_links (int): The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute.
                first_seen (str): The date we first found a link with a given anchor on your target.
                linked_pages (int): The number of unique pages linked from your target with a given anchor.
                links_from_target (int): The number of outbound links your target has with a given anchor.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerLinkedAnchorsInternalRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "linked-anchors-internal", request, SiteExplorerLinkedAnchorsInternalResponse, exclude_none=True)

    async def site_explorer_linkeddomains(
        self,
        request: SiteExplorerLinkeddomainsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerLinkeddomainsResponse:
        """
        Linked Domains.

        Args:
            request: SiteExplorerLinkeddomainsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerLinkeddomainsResponse containing SiteExplorerLinkeddomainsData:
                dofollow_linked_domains (int): The number of unique root domains with dofollow links linked from the linked domain.
                dofollow_links (int): The number of links from your target to the linked domain that don’t have the “nofollow” attribute.
                dofollow_refdomains (int): (5 units) The number of unique domains with dofollow links to the linked domain.
                domain (str): A linked domain that has at least one link from your target.
                domain_rating (float): The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.
                first_seen (str): The date we first found a link to the linked domain from your target.
                is_root_domain (bool): The domain name is a root domain name.
                linked_domain_traffic (int): (10 units) The linked domain’s estimated monthly organic traffic from search
                linked_pages (int): The number of the domain's pages linked from your target.
                links_from_target (int): The number of links to the linked domain from your target.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerLinkeddomainsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "linkeddomains", request, SiteExplorerLinkeddomainsResponse, exclude_none=True)

    async def site_explorer_metrics(
        self,
        request: SiteExplorerMetricsRequest | None = None,
        *,
        volume_mode: VolumeModeEnum | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerMetricsResponse:
        """
        Metrics.

        Args:
            request: SiteExplorerMetricsRequest
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerMetricsResponse containing SiteExplorerMetricsData:
                org_keywords (int): The total number of keywords that your target ranks for in the top 100 organic search results.
                paid_keywords (int): The total number of keywords that your target ranks for in paid search results.
                org_keywords_1_3 (int): The total number of keywords that your target ranks for in the top 3 organic search results.
                org_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from organic search.
                org_cost (int | None): (10 units) The estimated value of your target's monthly organic search traffic, in USD cents.
                paid_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from paid search.
                paid_cost (int | None): (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.
                paid_pages (int): The total number of pages from a target ranking in paid search results.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerMetricsRequest(**{k: v for k, v in [("volume_mode", volume_mode), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "metrics", request, SiteExplorerMetricsResponse, exclude_none=True)

    async def site_explorer_metrics_by_country(
        self,
        request: SiteExplorerMetricsByCountryRequest | None = None,
        *,
        select: SelectStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerMetricsByCountryResponse:
        """
        Metrics by country.

        Args:
            request: SiteExplorerMetricsByCountryRequest
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'paid_cost,paid_keywords,org_cost,paid_pages,org_keywords_1_3,org_keywords,org_traffic,paid_traffic,country'.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerMetricsByCountryResponse containing SiteExplorerMetricsByCountryData:
                country (CountryEnum1)
                org_cost (int | None): (10 units) The estimated value of your target's monthly organic search traffic, in USD cents.
                org_keywords (int): The total number of keywords that your target ranks for in the top 100 organic search results.
                org_keywords_1_3 (int): The total number of keywords that your target ranks for in the top 3 organic search results.
                org_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from organic search.
                paid_cost (int | None): (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.
                paid_keywords (int): The total number of keywords that your target ranks for in paid search results.
                paid_pages (int): The total number of pages from a target ranking in the top 100 paid search results.
                paid_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from paid search.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerMetricsByCountryRequest(**{k: v for k, v in [("select", select), ("volume_mode", volume_mode), ("protocol", protocol), ("target", target), ("mode", mode), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "metrics-by-country", request, SiteExplorerMetricsByCountryResponse, exclude_none=True)

    async def site_explorer_metrics_history(
        self,
        request: SiteExplorerMetricsHistoryRequest | None = None,
        *,
        select: SelectStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerMetricsHistoryResponse:
        """
        Metrics history.

        Args:
            request: SiteExplorerMetricsHistoryRequest
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'date,org_cost,org_traffic,paid_cost,paid_traffic'.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerMetricsHistoryResponse containing SiteExplorerMetricsHistoryData:
                date (str)
                org_cost (int): (10 units) The estimated cost of your target's monthly organic search traffic, in USD cents.
                org_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from organic search.
                paid_cost (int): (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.
                paid_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from paid search.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerMetricsHistoryRequest(**{k: v for k, v in [("select", select), ("volume_mode", volume_mode), ("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "metrics-history", request, SiteExplorerMetricsHistoryResponse, exclude_none=True)

    async def site_explorer_organic_competitors(
        self,
        request: SiteExplorerOrganicCompetitorsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerOrganicCompetitorsResponse:
        """
        Organic competitors.

        Args:
            request: SiteExplorerOrganicCompetitorsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerOrganicCompetitorsResponse containing SiteExplorerOrganicCompetitorsData:
                competitor_domain (str | None): A competitor's domain of your target in “domains" group mode.
                competitor_url (str | None): A competitor's URL of your target in pages" group mode.
                domain_rating (float): The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.
                group_mode (GroupModeEnum): To see competing pages instead, use the “exact URL” target mode or “path” target mode if your target doesn't have multiple pages.
                keywords_common (int): Organic keywords that both your target and a competitor are ranking for.
                keywords_competitor (int): Organic keywords that a competitor is ranking for, but your target isn't.
                keywords_target (int): Organic keywords that your target is ranking for, but a competitor isn't.
                pages (int | None): The total number of pages from a target ranking in search results.
                pages_diff (int): The change in pages between your selected dates.
                pages_merged (int): The pages field optimized for sorting.
                pages_prev (int | None): The total number of pages from a target ranking in search results on the comparison date.
                share (float): The percentage of common keywords out of the total number of keywords that your target and a competitor both rank for.
                traffic (int | None): (10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
                traffic_diff (int): The change in traffic between your selected dates.
                traffic_merged (int): (10 units) The traffic field optimized for sorting.
                traffic_prev (int | None): (10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter on the comparison date.
                value (int | None): (10 units) The estimated value of a page's monthly organic search traffic, in USD cents.
                value_diff (int): The change in value between your selected dates.
                value_merged (int | None): (10 units) The value field optimized for sorting.
                value_prev (int | None): (10 units) The estimated value of a page's monthly organic search traffic, in USD cents on the comparison date.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("country", country), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerOrganicCompetitorsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "organic-competitors", request, SiteExplorerOrganicCompetitorsResponse, exclude_none=True)

    async def site_explorer_organic_keywords(
        self,
        request: SiteExplorerOrganicKeywordsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerOrganicKeywordsResponse:
        """
        Organic keywords.

        Args:
            request: SiteExplorerOrganicKeywordsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerOrganicKeywordsResponse containing SiteExplorerOrganicKeywordsData:
                all_positions (list[dict[str, Any] | None]): (5 units) The list of all positions for a keyword.
                all_positions_prev (list[dict[str, Any] | None]): (5 units) The list of all positions for a keyword on the comparison date.
                best_position (int | None): The top position your target ranks for in the organic search results for a keyword.
                best_position_diff (int | None): The change in position between your selected dates.
                best_position_has_thumbnail (bool | None): The top position has a thumbnail.
                best_position_has_thumbnail_prev (bool | None): The top position has a thumbnail on the comparison date.
                best_position_has_video (bool | None): The top position has a video.
                best_position_has_video_prev (bool | None): The top position has a video on the comparison date.
                best_position_kind (BestPositionKindEnum | None): The kind of the top position: organic, paid, or a SERP feature.
                best_position_kind_merged (BestPositionKindEnum): The kind of the top position optimized for sorting.
                best_position_kind_prev (BestPositionKindEnum | None): The kind of the top position on the comparison date.
                best_position_prev (int | None): The top position on the comparison date.
                best_position_set (BestPositionSetEnum): The ranking group of the top position.
                best_position_set_prev (BestPositionSetEnum | None): The ranking group of the top position on the comparison date.
                best_position_url (str | None): The ranking URL in organic search results.
                best_position_url_prev (str | None): The ranking URL on the comparison date.
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cpc_merged (int | None): The CPC field optimized for sorting.
                cpc_prev (int | None): The CPC metric on the comparison date.
                entities (list[dict[str, Any] | None]): Organizations, products, persons, works, events, and locations found in a keyword.
                is_best_position_set_top_11_50 (bool): The ranking group of the top position is 11-50.
                is_best_position_set_top_11_50_prev (bool | None): The ranking group of the top position was 11-50 on the comparison date.
                is_best_position_set_top_3 (bool): The ranking group of the top position is Top 3.
                is_best_position_set_top_3_prev (bool | None): The ranking group of the top position was Top 3 on the comparison date.
                is_best_position_set_top_4_10 (bool): The ranking group of the top position is 4-10.
                is_best_position_set_top_4_10_prev (bool | None): The ranking group of the top position was 4-10 on the comparison date.
                is_branded (bool): User intent: branded. The user is searching for a specific brand or company name.
                is_commercial (bool): User intent: commercial. The user is comparing products or services before making a purchase decision.
                is_informational (bool): User intent: informational. The user is looking for information or an answer to a specific question.
                is_local (bool): User intent: local. The user is looking for information relevant to a specific location or nearby services.
                ... and 37 more fields. See SiteExplorerOrganicKeywordsData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerOrganicKeywordsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "organic-keywords", request, SiteExplorerOrganicKeywordsResponse, exclude_none=True)

    async def site_explorer_outlinks_stats(
        self,
        request: SiteExplorerOutlinksStatsRequest | None = None,
        *,
        protocol: ProtocolEnum | None = None,
        mode: ModeEnum | None = None,
        target: str | None = None,
    ) -> SiteExplorerOutlinksStatsResponse:
        """
        Outlinks stats.

        **This is a beta version of the endpoint. The data it returns may not always exactly match the corresponding values in Ahrefs UI. Data accuracy will be improved soon.**

        Args:
            request: SiteExplorerOutlinksStatsRequest
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                target (str, required): The target of the search: a domain or a URL.

        Returns:
            SiteExplorerOutlinksStatsResponse containing SiteExplorerOutlinksStatsData:
                outgoing_links (int): The number of external links from the target.
                outgoing_links_dofollow (int): The number of external dofollow links from the target.
                linked_domains (int): The number of unique root domains linked from the target.
                linked_domains_dofollow (int): The number of unique root domains linked via dofollow links from the target.
        """
        if request is None:
            _missing = [k for k, v in [("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerOutlinksStatsRequest(**{k: v for k, v in [("protocol", protocol), ("mode", mode), ("target", target)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "outlinks-stats", request, SiteExplorerOutlinksStatsResponse, exclude_none=True)

    async def site_explorer_pages_by_traffic(
        self,
        request: SiteExplorerPagesByTrafficRequest | None = None,
        *,
        volume_mode: VolumeModeEnum | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerPagesByTrafficResponse:
        """
        Pages by traffic.

        Args:
            request: SiteExplorerPagesByTrafficRequest
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerPagesByTrafficResponse containing SiteExplorerPagesByTrafficData:
                range0_pages (int): The total number of pages with 0 traffic.
                range100_traffic (int): (10 units) The total traffic from pages with 1-100 traffic.
                range100_pages (int): The total number of pages with 1-100 traffic.
                range1k_traffic (int): (10 units) The total traffic from pages with 101-1K traffic.
                range1k_pages (int): The total number of pages with 101-1K traffic.
                range5k_traffic (int): (10 units) The total traffic from pages with 1K-5K traffic.
                range5k_pages (int): The total number of pages with 1K-5K traffic.
                range10k_traffic (int): (10 units) The total traffic from pages with 5K-10K traffic.
                range10k_pages (int): The total number of pages with 5K-10K traffic.
                range10k_plus_traffic (int): (10 units) The total traffic from pages with 10K+ traffic.
                range10k_plus_pages (int): The total number of pages with 10K+ traffic.
        """
        if request is None:
            _missing = [k for k, v in [("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerPagesByTrafficRequest(**{k: v for k, v in [("volume_mode", volume_mode), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "pages-by-traffic", request, SiteExplorerPagesByTrafficResponse, exclude_none=True)

    async def site_explorer_pages_history(
        self,
        request: SiteExplorerPagesHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerPagesHistoryResponse:
        """
        Pages history.

        Args:
            request: SiteExplorerPagesHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerPagesHistoryResponse containing SiteExplorerPagesHistoryData:
                date (str)
                pages (int): The total number of pages from a target ranking in the top 100 organic search results.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerPagesHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "pages-history", request, SiteExplorerPagesHistoryResponse, exclude_none=True)

    async def site_explorer_paid_pages(
        self,
        request: SiteExplorerPaidPagesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerPaidPagesResponse:
        """
        Paid pages.

        Args:
            request: SiteExplorerPaidPagesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerPaidPagesResponse containing SiteExplorerPaidPagesData:
                ads_count (int | None): The number of unique ads with a page.
                ads_count_diff (int): The change in ads between your selected dates.
                ads_count_prev (int | None): The number of ads on the comparison date.
                keywords (int | None): The total number of keywords that your target ranks for in paid search results.
                keywords_diff (int): The change in keywords between your selected dates.
                keywords_diff_percent (int): The change in keywords between your selected dates, in percents.
                keywords_merged (int): The total number of keywords optimized for sorting.
                keywords_prev (int | None): The keyword your target ranks for on the comparison date.
                raw_url (str): The ranking page URL in encoded format.
                raw_url_prev (str | None): The ranking page URL on the comparison date in encoded format.
                referring_domains (int | None): (5 units) The number of unique domains linking to a page.
                status (StatusEnum): The status of a page: the new page that just started to rank in paid results ("left"), the lost page that disappeared from paid results ("right"), or no change ("both").
                sum_traffic (int | None): (10 units) An estimation of the monthly paid search traffic that a page gets from all the keywords that it ranks for.
                sum_traffic_merged (int): (10 units) The paid traffic field optimized for sorting.
                sum_traffic_prev (int | None): (10 units) The paid traffic on the comparison date.
                top_keyword (str | None): The keyword that brings the most paid traffic to a page.
                top_keyword_best_position (int | None): The ranking position that a page holds for its top keyword.
                top_keyword_best_position_diff (int | None): The change in the top position between your selected dates.
                top_keyword_best_position_kind (BestPositionKindEnum | None): The kind of the top position: organic, paid or a SERP feature.
                top_keyword_best_position_kind_prev (BestPositionKindEnum | None): The kind of the top position on the comparison date.
                top_keyword_best_position_prev (int | None): The top position on the comparison date.
                top_keyword_best_position_title (str | None): The title displayed for the page in its top keyword's SERP.
                top_keyword_best_position_title_prev (str | None): The title displayed for the page in its top keyword's SERP on the comparison date.
                top_keyword_country (CountryEnum1 | None): The country in which a page ranks for its top keyword.
                top_keyword_country_prev (CountryEnum1 | None): The country in which a page ranks for its top keyword on the comparison date.
                top_keyword_prev (str | None): The keyword that brings the most paid traffic to a page on the comparison date.
                top_keyword_volume (int | None): (10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
                top_keyword_volume_prev (int | None): (10 units) The search volume on the comparison date.
                traffic_diff (int): The change in traffic between your selected dates.
                traffic_diff_percent (int): The change in traffic between your selected dates, in percents.
                ... and 8 more fields. See SiteExplorerPaidPagesData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerPaidPagesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "paid-pages", request, SiteExplorerPaidPagesResponse, exclude_none=True)

    async def site_explorer_refdomains(
        self,
        request: SiteExplorerRefdomainsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerRefdomainsResponse:
        """
        Refdomains.

        Args:
            request: SiteExplorerRefdomainsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerRefdomainsResponse containing SiteExplorerRefdomainsData:
                dofollow_linked_domains (int): The number of unique root domains with dofollow links linked from the referring domain.
                dofollow_links (int): The number of links from the referring domain to your target that don't have the “nofollow” attribute.
                dofollow_refdomains (int): (5 units) The number of unique domains with dofollow links to the referring domain.
                domain (str): A referring domain that has at least one link to your target.
                domain_rating (float): The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.
                first_seen (str): The date we first found a backlink to your target from the referring domain.
                ip_source (str | None): The referring domain IP address.
                is_root_domain (bool): The domain name is a root domain name.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                last_seen (str | None): The date your target lost its last live backlink for the referring domain.
                links_to_target (int): The number of backlinks from the referring domain to your target.
                lost_links (int): The number of backlinks lost from the referring domain for the selected time period.
                new_links (int): The number of new backlinks found from the referring domain for the selected time period.
                positions_source_domain (int): The number of keywords that the referring domain ranks for in the top 100 positions.
                traffic_domain (int): (10 units) The referring domain's estimated monthly organic traffic from search.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerRefdomainsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "refdomains", request, SiteExplorerRefdomainsResponse, exclude_none=True)

    async def site_explorer_refdomains_history(
        self,
        request: SiteExplorerRefdomainsHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerRefdomainsHistoryResponse:
        """
        Refdomains history.

        Args:
            request: SiteExplorerRefdomainsHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerRefdomainsHistoryResponse containing SiteExplorerRefdomainsHistoryData:
                date (str)
                refdomains (int): (5 units) The total number of unique domains linking to your target.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerRefdomainsHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "refdomains-history", request, SiteExplorerRefdomainsHistoryResponse, exclude_none=True)

    async def site_explorer_top_pages(
        self,
        request: SiteExplorerTopPagesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerTopPagesResponse:
        """
        Top pages.

        Args:
            request: SiteExplorerTopPagesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerTopPagesResponse containing SiteExplorerTopPagesData:
                keywords (int | None): The total number of keywords that your target ranks for in the top 100 organic search results.
                keywords_diff (int): The change in keywords between your selected dates.
                keywords_diff_percent (int): The change in keywords between your selected dates, in percents.
                keywords_merged (int): The total number of keywords optimized for sorting.
                keywords_prev (int | None): The keyword your target ranks for on the comparison date.
                raw_url (str): The ranking page URL in encoded format.
                raw_url_prev (str | None): The ranking page URL on the comparison date in encoded format.
                referring_domains (int | None): (5 units) The number of unique domains linking to a page.
                status (StatusEnum): The status of a page: the new page that just started to rank ("left"), the lost page that disappeared from search results ("right"), or no change ("both").
                sum_traffic (int | None): (10 units) An estimation of the monthly organic search traffic that a page gets from all the keywords that it ranks for.
                sum_traffic_merged (int): (10 units) The traffic field optimized for sorting.
                sum_traffic_prev (int | None): (10 units) The traffic on the comparison date.
                top_keyword (str | None): The keyword that brings the most organic traffic to a page.
                top_keyword_best_position (int | None): The ranking position that a page holds for its top keyword.
                top_keyword_best_position_diff (int | None): The change in the top position between your selected dates.
                top_keyword_best_position_kind (BestPositionKindEnum | None): The kind of the top position: organic, paid or a SERP feature.
                top_keyword_best_position_kind_prev (BestPositionKindEnum | None): The kind of the top position on the comparison date.
                top_keyword_best_position_prev (int | None): The top position on the comparison date.
                top_keyword_best_position_title (str | None): The title displayed for the page in its top keyword's SERP.
                top_keyword_best_position_title_prev (str | None): The title displayed for the page in its top keyword's SERP on the comparison date.
                top_keyword_country (CountryEnum1 | None): The country in which a page ranks for its top keyword.
                top_keyword_country_prev (CountryEnum1 | None): The country in which a page ranks for its top keyword on the comparison date.
                top_keyword_prev (str | None): The keyword that brings the most organic traffic to a page on the comparison date.
                top_keyword_volume (int | None): (10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
                top_keyword_volume_prev (int | None): (10 units) The search volume on the comparison date.
                traffic_diff (int): The change in traffic between your selected dates.
                traffic_diff_percent (int): The change in traffic between your selected dates, in percents.
                ur (float | None): URL Rating (UR) shows the strength of your target page’s backlink profile on a 100-point logarithmic scale.
                url (str | None): The ranking page URL.
                url_prev (str | None): The ranking page URL on the comparison date.
                ... and 5 more fields. See SiteExplorerTopPagesData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerTopPagesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "top-pages", request, SiteExplorerTopPagesResponse, exclude_none=True)

    async def site_explorer_total_search_volume_history(
        self,
        request: SiteExplorerTotalSearchVolumeHistoryRequest | None = None,
        *,
        volume_mode: VolumeModeEnum | None = None,
        top_positions: ViewForEnum | None = None,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerTotalSearchVolumeHistoryResponse:
        """
        Total search volume history.

        Args:
            request: SiteExplorerTotalSearchVolumeHistoryRequest
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                top_positions (ViewForEnum, optional): The number of top organic search positions to consider when calculating total search volume. Default: 'top_10'.
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerTotalSearchVolumeHistoryResponse containing SiteExplorerTotalSearchVolumeHistoryData:
                date (str)
                total_search_volume (int): (10 units) The total search volume of keywords for which your target ranks within the specified `top_positions` in the search results.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerTotalSearchVolumeHistoryRequest(**{k: v for k, v in [("volume_mode", volume_mode), ("top_positions", top_positions), ("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "total-search-volume-history", request, SiteExplorerTotalSearchVolumeHistoryResponse, exclude_none=True)

    async def site_explorer_url_rating_history(
        self,
        request: SiteExplorerUrlRatingHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        target: str | None = None,
    ) -> SiteExplorerUrlRatingHistoryResponse:
        """
        URL Rating history.

        Args:
            request: SiteExplorerUrlRatingHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                target (str, required): The target of the search: a domain or a URL.

        Returns:
            SiteExplorerUrlRatingHistoryResponse containing SiteExplorerUrlRatingHistoryData:
                date (str)
                url_rating (float): The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerUrlRatingHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("target", target)] if v is not None})  # pyright: ignore[reportArgumentType]
        return await self._request("site-explorer", "url-rating-history", request, SiteExplorerUrlRatingHistoryResponse, exclude_none=True)

    # fmt: on


class GeneratedSyncMethodsMixin:
    """Sync endpoint methods. Mixed into AhrefsClient."""

    def _request(
        self, api_section: str, endpoint: str, request_model: BaseModel,
        response_model_class: type[T], *, exclude_none: bool = False,
    ) -> T:
        raise NotImplementedError

    # fmt: off
    # Brand Radar API methods
    def brand_radar_ai_responses(
        self,
        request: BrandRadarAiResponsesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        date: DateStr | None = None,
        country: CountryEnum | None = None,
        order_by: OrderByEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarAiResponsesResponse:
        """
        AI Responses.

        Args:
            request: BrandRadarAiResponsesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date (str, optional): The date to search for in YYYY-MM-DD format. Default: None.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                order_by (OrderByEnum, optional): The order by field. Default: 'relevance'.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. Default: '[]'.

        Returns:
            BrandRadarAiResponsesResponse containing BrandRadarAiResponsesData:
                country (str): The country of the question.
                links (list[dict[str, Any] | None]): (10 units) The links used for the response.
                question (str): The question asked by the user.
                response (str): (10 units) The response from the model.
                volume (int): (10 units) Estimated monthly searches. This is based on our estimates for Google, combining the search volumes of related keywords where this question appears in People Also Ask section.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarAiResponsesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("where", where), ("select", select), ("date", date), ("country", country), ("order_by", order_by), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("brand-radar", "ai-responses", request, BrandRadarAiResponsesResponse, exclude_none=True)

    def brand_radar_impressions_history(
        self,
        request: BrandRadarImpressionsHistoryRequest | None = None,
        *,
        where: str | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarImpressionsHistoryResponse:
        """
        Overview history - Impressions.

        Args:
            request: BrandRadarImpressionsHistoryRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brand. Default: '[]'.
                brand (str, required): The brand to search for.

        Returns:
            BrandRadarImpressionsHistoryResponse containing BrandRadarImpressionsHistoryData:
                date (str): date
                impressions (int): impressions
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("data_source", data_source), ("brand", brand)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarImpressionsHistoryRequest(**{k: v for k, v in [("where", where), ("date_to", date_to), ("date_from", date_from), ("country", country), ("data_source", data_source), ("market", market), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("brand-radar", "impressions-history", request, BrandRadarImpressionsHistoryResponse, exclude_none=True)

    def brand_radar_impressions_overview(
        self,
        request: BrandRadarImpressionsOverviewRequest | None = None,
        *,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarImpressionsOverviewResponse:
        """
        Overview - Impressions.

        Args:
            request: BrandRadarImpressionsOverviewRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand or competitors should not be empty. Default: '[]'.

        Returns:
            BrandRadarImpressionsOverviewResponse containing BrandRadarImpressionsOverviewData:
                brand (str): Brand name (either your brand or a competitor provided in the request).
                no_tracked_brands (int): Estimated impressions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified).
                only_competitors_brands (int): Estimated impressions from responses mentioning only competitor brands.
                only_target_brand (int): Estimated impressions from responses mentioning only your brand.
                target_and_competitors_brands (int): Estimated impressions from responses mentioning both your and competitor brands.
                total (int): Total estimated impressions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`).
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarImpressionsOverviewRequest(**{k: v for k, v in [("where", where), ("select", select), ("country", country), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("brand-radar", "impressions-overview", request, BrandRadarImpressionsOverviewResponse, exclude_none=True)

    def brand_radar_mentions_history(
        self,
        request: BrandRadarMentionsHistoryRequest | None = None,
        *,
        where: str | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarMentionsHistoryResponse:
        """
        Overview history - Mentions.

        Args:
            request: BrandRadarMentionsHistoryRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brand. Default: '[]'.
                brand (str, required): The brand to search for.

        Returns:
            BrandRadarMentionsHistoryResponse containing BrandRadarMentionsHistoryData:
                date (str): date
                mentions (int): mentions
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("data_source", data_source), ("brand", brand)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarMentionsHistoryRequest(**{k: v for k, v in [("where", where), ("date_to", date_to), ("date_from", date_from), ("country", country), ("data_source", data_source), ("market", market), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("brand-radar", "mentions-history", request, BrandRadarMentionsHistoryResponse, exclude_none=True)

    def brand_radar_mentions_overview(
        self,
        request: BrandRadarMentionsOverviewRequest | None = None,
        *,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarMentionsOverviewResponse:
        """
        Overview - Mentions.

        Args:
            request: BrandRadarMentionsOverviewRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand or competitors should not be empty. Default: '[]'.

        Returns:
            BrandRadarMentionsOverviewResponse containing BrandRadarMentionsOverviewData:
                brand (str): Brand name (either your brand or a competitor provided in the request).
                no_tracked_brands (int): Estimated mentions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified).
                only_competitors_brands (int): Estimated mentions from responses mentioning only competitor brands.
                only_target_brand (int): Estimated mentions from responses mentioning only your brand.
                target_and_competitors_brands (int): Estimated mentions from responses mentioning both your and competitor brands.
                total (int): Total estimated mentions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`).
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarMentionsOverviewRequest(**{k: v for k, v in [("where", where), ("select", select), ("country", country), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("brand-radar", "mentions-overview", request, BrandRadarMentionsOverviewResponse, exclude_none=True)

    def brand_radar_sov_overview(
        self,
        request: BrandRadarSovOverviewRequest | None = None,
        *,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        data_source: DataSourceEnum | None = None,
        market: str | None = None,
        competitors: str | None = None,
        brand: str | None = None,
    ) -> BrandRadarSovOverviewResponse:
        """
        Overview - Share of Voice.

        Args:
            request: BrandRadarSovOverviewRequest
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                data_source (DataSourceEnum, required): The chatbot model to use.
                market (str, optional): A comma-separated list of the niche markets of your brands. Default: '[]'.
                competitors (str, optional): A comma-separated list of competitors of your brands. Default: '[]'.
                brand (str, optional): A comma-separated list of brands to search for. At least one of brand or competitors should not be empty. Default: '[]'.

        Returns:
            BrandRadarSovOverviewResponse containing BrandRadarSovOverviewData:
                brand (str): Brand name (either your brand or a competitor provided in the request).
                share_of_voice (float): Estimated share of voice for your brand.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("data_source", data_source)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = BrandRadarSovOverviewRequest(**{k: v for k, v in [("where", where), ("select", select), ("country", country), ("data_source", data_source), ("market", market), ("competitors", competitors), ("brand", brand)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("brand-radar", "sov-overview", request, BrandRadarSovOverviewResponse, exclude_none=True)

    # Keywords Explorer API methods
    def keywords_explorer_matching_terms(
        self,
        request: KeywordsExplorerMatchingTermsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        search_engine: SearchEngineEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
        match_mode: MatchModeEnum | None = None,
        terms: TermsEnum | None = None,
    ) -> KeywordsExplorerMatchingTermsResponse:
        """
        Matching terms.

        Args:
            request: KeywordsExplorerMatchingTermsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.
                match_mode (MatchModeEnum, optional): Keyword ideas contain the words from your query in any order (terms mode) or in the exact order they are written (phrase mode). Default: 'terms'.
                terms (TermsEnum, optional): All keywords ideas or keywords ideas phrased as questions. Default: 'all'.

        Returns:
            KeywordsExplorerMatchingTermsResponse containing KeywordsExplorerMatchingTermsData:
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerMatchingTermsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("country", country), ("search_engine", search_engine), ("keywords", keywords), ("keyword_list_id", keyword_list_id), ("match_mode", match_mode), ("terms", terms)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("keywords-explorer", "matching-terms", request, KeywordsExplorerMatchingTermsResponse, exclude_none=True)

    def keywords_explorer_overview(
        self,
        request: KeywordsExplorerOverviewRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        volume_monthly_date_to: DateStr | None = None,
        volume_monthly_date_from: DateStr | None = None,
        target_mode: ModeEnum | None = None,
        target: str | None = None,
        target_position: TargetPositionEnum | None = None,
        country: CountryEnum | None = None,
        search_engine: SearchEngineEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
    ) -> KeywordsExplorerOverviewResponse:
        """
        Overview.

        The `regex` filter has limited functionality when used in this request, and the syntax differs from other requests. It expects an asterisk (*) symbol as a wildcard.

        Args:
            request: KeywordsExplorerOverviewRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                volume_monthly_date_to (str, optional): The end date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested. Default: None.
                volume_monthly_date_from (str, optional): The start date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested. Default: None.
                target_mode (ModeEnum, optional): The scope of the target URL you specified. Default: None.
                target (str, optional): The target of the search: a domain or a URL. Default: None.
                target_position (TargetPositionEnum, optional): Filters keywords based on the ranking position of the specified `target`. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.

        Returns:
            KeywordsExplorerOverviewResponse containing KeywordsExplorerOverviewData:
                clicks (int | None): The average monthly number of clicks on the search results that people make while searching for the target keyword.
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                parent_volume (int | None): (10 units) The search volume of the parent topic.
                searches_pct_clicks_organic_and_paid (float | None): The average monthly percentage of people who clicked on both organic and paid results while searching for the target keyword.
                searches_pct_clicks_organic_only (float | None): The average monthly percentage of people who clicked only on organic results while searching for the target keyword.
                searches_pct_clicks_paid_only (float | None): The average monthly percentage of people who clicked only on paid results while searching for the target keyword.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
                volume_monthly_history (list[dict[str, Any] | None]): (2 units per historical month, with a minimum of 50 units) Historical monthly search volume estimates of a keyword for the period set by the `volume_monthly_date_from` and `volume_monthly_date_to` parameters.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerOverviewRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("volume_monthly_date_to", volume_monthly_date_to), ("volume_monthly_date_from", volume_monthly_date_from), ("target_mode", target_mode), ("target", target), ("target_position", target_position), ("country", country), ("search_engine", search_engine), ("keywords", keywords), ("keyword_list_id", keyword_list_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("keywords-explorer", "overview", request, KeywordsExplorerOverviewResponse, exclude_none=True)

    def keywords_explorer_related_terms(
        self,
        request: KeywordsExplorerRelatedTermsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
        view_for: ViewForEnum | None = None,
        terms: TermsEnum1 | None = None,
    ) -> KeywordsExplorerRelatedTermsResponse:
        """
        Related terms.

        Args:
            request: KeywordsExplorerRelatedTermsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.
                view_for (ViewForEnum, optional): View keywords for the top 10 or top 100 ranking pages. Default: 'top_10'.
                terms (TermsEnum1, optional): Related keywords which top-ranking pages also rank for (`also_rank_for`), additional keywords frequently mentioned in top-ranking pages (`also_talk_about`), or combination of both (`all`). Default: 'all'.

        Returns:
            KeywordsExplorerRelatedTermsResponse containing KeywordsExplorerRelatedTermsData:
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerRelatedTermsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("country", country), ("keywords", keywords), ("keyword_list_id", keyword_list_id), ("view_for", view_for), ("terms", terms)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("keywords-explorer", "related-terms", request, KeywordsExplorerRelatedTermsResponse, exclude_none=True)

    def keywords_explorer_search_suggestions(
        self,
        request: KeywordsExplorerSearchSuggestionsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        country: CountryEnum | None = None,
        search_engine: SearchEngineEnum | None = None,
        keywords: str | None = None,
        keyword_list_id: int | None = None,
    ) -> KeywordsExplorerSearchSuggestionsResponse:
        """
        Search suggestions.

        Args:
            request: KeywordsExplorerSearchSuggestionsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keywords (str, optional): A comma-separated list of keywords to show metrics for. Default: None.
                keyword_list_id (int, optional): The id of an existing keyword list to show metrics for. Default: None.

        Returns:
            KeywordsExplorerSearchSuggestionsResponse containing KeywordsExplorerSearchSuggestionsData:
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cps (float | None): Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                difficulty (int | None): (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                first_seen (str | None): The date when we first checked search engine results for a keyword.
                global_volume (int | None): (10 units) How many times per month, on average, people search for the target keyword across all countries in our database.
                intents (dict[str, Any] | None): (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.
                keyword (str)
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                serp_features (list[SerpFeaturesItemEnum | None]): The enriched results on a search engine results page (SERP) that are not traditional organic results.
                serp_last_update (str | None): The date when we last checked search engine results for a keyword.
                traffic_potential (int | None): (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.
                volume (int | None): (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.
                volume_desktop_pct (float | None): The percentage of searches for a keyword performed on desktop devices.
                volume_mobile_pct (float | None): The percentage of searches for a keyword performed on mobile devices.
                volume_monthly (int | None): (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerSearchSuggestionsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("country", country), ("search_engine", search_engine), ("keywords", keywords), ("keyword_list_id", keyword_list_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("keywords-explorer", "search-suggestions", request, KeywordsExplorerSearchSuggestionsResponse, exclude_none=True)

    def keywords_explorer_volume_by_country(
        self,
        request: KeywordsExplorerVolumeByCountryRequest | None = None,
        *,
        limit: int | None = None,
        search_engine: SearchEngineEnum | None = None,
        keyword: str | None = None,
    ) -> KeywordsExplorerVolumeByCountryResponse:
        """
        Volume by country.

        Args:
            request: KeywordsExplorerVolumeByCountryRequest
                limit (int, optional): The number of results to return. Default: None.
                search_engine (SearchEngineEnum, optional): [Deprecated on 5 Aug 2024]. Default: 'google'.
                keyword (str, required): The keyword to show metrics for.

        Returns:
            KeywordsExplorerVolumeByCountryResponse containing KeywordsExplorerVolumeByCountryData:
                country (str)
                volume (int): (10 units) An estimation of the average monthly number of searches for a keyword in a given country.
        """
        if request is None:
            _missing = [k for k, v in [("keyword", keyword)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerVolumeByCountryRequest(**{k: v for k, v in [("limit", limit), ("search_engine", search_engine), ("keyword", keyword)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("keywords-explorer", "volume-by-country", request, KeywordsExplorerVolumeByCountryResponse, exclude_none=True)

    def keywords_explorer_volume_history(
        self,
        request: KeywordsExplorerVolumeHistoryRequest | None = None,
        *,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        keyword: str | None = None,
    ) -> KeywordsExplorerVolumeHistoryResponse:
        """
        Volume history.

        Args:
            request: KeywordsExplorerVolumeHistoryRequest
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, optional): The start date of the historical period in YYYY-MM-DD format. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                keyword (str, required): The keyword to show metrics for.

        Returns:
            KeywordsExplorerVolumeHistoryResponse containing KeywordsExplorerVolumeHistoryData:
                date (str)
                volume (int): An estimation of the number of searches for a keyword over a given month.
        """
        if request is None:
            _missing = [k for k, v in [("country", country), ("keyword", keyword)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = KeywordsExplorerVolumeHistoryRequest(**{k: v for k, v in [("date_to", date_to), ("date_from", date_from), ("country", country), ("keyword", keyword)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("keywords-explorer", "volume-history", request, KeywordsExplorerVolumeHistoryResponse, exclude_none=True)

    # Rank Tracker API methods
    def rank_tracker_competitors_overview(
        self,
        request: RankTrackerCompetitorsOverviewRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerCompetitorsOverviewResponse:
        """
        Competitors overview.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerCompetitorsOverviewRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerCompetitorsOverviewResponse containing RankTrackerCompetitorsOverviewData:
                competitors_list (list[dict[str, Any] | None]): Competitors information for a given keyword. The following fields are included: `url`, `url_prev`, `position`, `position_prev`, `best_position_kind`, `best_position_kind`, `traffic`, `traffic_prev`, `value`, `value_prev`. Fields ending in `prev` are included only in the compared view.
                country (CountryEnum1): The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2).
                keyword (str): The keyword your target ranks for.
                keyword_difficulty (int | None): An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                keyword_has_data (bool): Will return `false` if the keyword is still processing and no SERP has been fetched yet.
                keyword_is_frozen (bool): Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are "frozen", meaning they do not have their rankings updated.
                language (str): The SERP language that a given keyword is being tracked for.
                location (str): The location (country, state/province, or city) that a given keyword is being tracked in.
                serp_features (list[SerpFeaturesItemEnum1 | None]): The SERP features that appear in search results for a keyword.
                serp_updated (str | None): The date when we last checked search engine results for a keyword.
                serp_updated_prev (str | None): The date when we checked search engine results up to the comparison date.
                tags (list[str | None]): A list of tags assigned to a given keyword.
                volume (int | None): An estimation of the average monthly number of searches for a keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerCompetitorsOverviewRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("date_compared", date_compared), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("rank-tracker", "competitors-overview", request, RankTrackerCompetitorsOverviewResponse, exclude_none=True)

    def rank_tracker_competitors_pages(
        self,
        request: RankTrackerCompetitorsPagesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        target_and_tracked_competitors_only: bool | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerCompetitorsPagesResponse:
        """
        Competitors pages.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerCompetitorsPagesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                target_and_tracked_competitors_only (bool, optional): Restrict pages to target and tracked competitors Default: False.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerCompetitorsPagesResponse containing RankTrackerCompetitorsPagesData:
                keywords (int): The total number of keywords that your target ranks for in the top 100 organic search results.
                share_of_traffic_value (float): The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords.
                share_of_traffic_value_prev (float): The share of traffic value on the comparison date.
                share_of_voice (float): The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords.
                share_of_voice_prev (float): The share of voice on the comparison date.
                status (StatusEnum): The status of a page: the new page that just started to rank ("left"), the lost page that disappeared from search results ("right"), or no change ("both").
                title (str | None): The title displayed for the page in its top keyword's SERP.
                title_prev (str | None): The title on the comparison date.
                traffic (int): An estimation of the number of monthly visits that a page gets from organic search.
                traffic_prev (int): The traffic on the comparison date.
                traffic_value (int | None): The estimated value of a page’s monthly organic search traffic, in USD cents.
                traffic_value_prev (int | None): The traffic value on the comparison date.
                url (str): The page URL.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerCompetitorsPagesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("target_and_tracked_competitors_only", target_and_tracked_competitors_only), ("date_compared", date_compared), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("rank-tracker", "competitors-pages", request, RankTrackerCompetitorsPagesResponse, exclude_none=True)

    def rank_tracker_competitors_stats(
        self,
        request: RankTrackerCompetitorsStatsRequest | None = None,
        *,
        select: SelectStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerCompetitorsStatsResponse:
        """
        Competitors metrics.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerCompetitorsStatsRequest
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerCompetitorsStatsResponse containing RankTrackerCompetitorsStatsData:
                ai_overview_count (int): The total number of tracked keywords for which your target ranks in an AI Overview.
                average_position (float | None): The average of your target's top organic positions across all tracked keywords.
                competitor (str): Competitor's URL.
                discussions_count (int): The total number of tracked keywords for which your target ranks in Discussions and forums.
                featured_snippet_count (int): The total number of tracked keywords for which your target ranks in a Featured snippet.
                image_pack_count (int): The total number of tracked keywords for which your target ranks in an Image pack.
                knowledge_card_count (int): The total number of tracked keywords for which your target ranks in a Knowledge card.
                knowledge_panel_count (int): The total number of tracked keywords for which your target ranks in a Knowledge panel.
                pos_11_20 (int): The total number of tracked keywords for which your target's top organic position is within the 11th to 20th results.
                pos_1_3 (int): The total number of tracked keywords for which your target's top organic position is within the top 3 results.
                pos_21_50 (int): The total number of tracked keywords for which your target's top organic position is within the 21st to 50th results.
                pos_4_10 (int): The total number of tracked keywords for which your target's top organic position is within the 4th to 10th results.
                pos_51_plus (int): The total number of tracked keywords for which your target's top organic position is the 51st or higher.
                pos_no_rank (int): The total number of tracked keywords where your target doesn't rank.
                share_of_traffic_value (float): The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords.
                share_of_voice (float): The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords.
                sitelinks_count (int): The total number of tracked keywords for which your target ranks in Sitelinks.
                thumbnail_count (int): The total number of tracked keywords for which your target ranks in a Thumbnail.
                top_stories_count (int): The total number of tracked keywords for which your target ranks in Top stories.
                traffic (int | None): The estimated number of monthly visits that your target gets from organic search for all tracked keywords.
                traffic_value (int | None): The estimated value of your target's monthly organic search traffic for all tracked keywords.
                video_preview_count (int): The total number of tracked keywords for which your target ranks in a Video preview.
                videos_count (int): The total number of tracked keywords for which your target ranks in Videos.
                x_count (int): The total number of tracked keywords for which your target ranks in an X (Twitter) widget.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerCompetitorsStatsRequest(**{k: v for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("rank-tracker", "competitors-stats", request, RankTrackerCompetitorsStatsResponse, exclude_none=True)

    def rank_tracker_overview(
        self,
        request: RankTrackerOverviewRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        device: DeviceEnum | None = None,
        project_id: int | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> RankTrackerOverviewResponse:
        """
        Overview.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerOverviewRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            RankTrackerOverviewResponse containing RankTrackerOverviewData:
                best_position_has_thumbnail (bool | None): The top position (or target URL’s, if set) has a thumbnail.
                best_position_has_thumbnail_previous (bool | None): The top position (or target URL’s, if set) has a thumbnail on the comparison date.
                best_position_has_video_preview (bool | None): The top position (or target URL’s, if set) has a video preview.
                best_position_has_video_preview_previous (bool | None): The top position (or target URL’s, if set) has a video preview on the comparison date.
                best_position_kind (BestPositionKindEnum | None): The kind of top position (or target URL’s, if set): organic, paid, or a SERP feature.
                best_position_kind_previous (BestPositionKindEnum | None): The kind of top position (or target URL’s, if set) on the comparison date.
                clicks (int | None): Clicks metric refers to the average monthly number of clicks on the search results that people make while searching for the target keyword. Some searches generate clicks on multiple results, while others might not end in any clicks at all.
                clicks_per_search (float | None): Clicks Per Search is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.
                cost_per_click (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword.
                country (CountryEnum1): The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2).
                country_prev (CountryEnum1): The country that a given keyword is being tracked in on the comparison date. A two-letter country code (ISO 3166-1 alpha-2).
                created_at (str): The date when a keyword was added to the project.
                is_branded (bool): User intent: branded. The user is searching for a specific brand or company name.
                is_commercial (bool): User intent: commercial. The user is comparing products or services before making a purchase decision.
                is_informational (bool): User intent: informational. The user is looking for information or an answer to a specific question.
                is_local (bool): User intent: local. The user is looking for information relevant to a specific location or nearby services.
                is_navigational (bool): User intent: navigational. The user is searching for a specific website or web page.
                is_transactional (bool): User intent: transactional. The user is ready to complete an action, often a purchase.
                keyword (str): The keyword your target ranks for.
                keyword_difficulty (int | None): An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.
                keyword_has_data (bool): Will return `false` if the keyword is still processing and no SERP has been fetched yet.
                keyword_is_frozen (bool): Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are "frozen", meaning they do not have their rankings updated.
                keyword_prev (str): The keyword your target ranks for on the comparison date.
                language (str): The SERP language that a given keyword is being tracked for.
                language_prev (str): The SERP language on the comparison date.
                location (str): The location (country, state/province, or city) that a given keyword is being tracked in.
                location_prev (str): The location (country, state/province, or city) that a given keyword is being tracked in on the comparison date.
                parent_topic (str | None): Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead.  To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.
                position (int | None): The top position (or target URL’s, if set) in organic search.
                position_diff (int | None): The change in top position (or target URL’s, if set) between selected dates.
                ... and 20 more fields. See RankTrackerOverviewData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("date", date), ("device", device), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerOverviewRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("date_compared", date_compared), ("date", date), ("device", device), ("project_id", project_id), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("rank-tracker", "overview", request, RankTrackerOverviewResponse, exclude_none=True)

    def rank_tracker_serp_overview(
        self,
        request: RankTrackerSerpOverviewRequest | None = None,
        *,
        top_positions: int | None = None,
        device: DeviceEnum | None = None,
        date: str | None = None,
        location_id: int | None = None,
        country: CountryEnum | None = None,
        language_code: str | None = None,
        keyword: str | None = None,
        project_id: int | None = None,
    ) -> RankTrackerSerpOverviewResponse:
        """
        SERP Overview.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: RankTrackerSerpOverviewRequest
                top_positions (int, optional): The number of top organic SERP positions to return. If not specified, all available positions will be returned. Default: None.
                device (DeviceEnum, required): Choose between mobile and desktop rankings.
                date (str, optional): A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned. Default: None.
                location_id (int, optional): The location ID of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                language_code (str, optional): The language code of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords. Default: None.
                keyword (str, required): The keyword to return SERP Overview for.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`

        Returns:
            RankTrackerSerpOverviewResponse containing RankTrackerSerpOverviewData:
                position (int): The position of the search result in SERP.
                title (str | None): The title of a ranking page.
                url (str | None): The URL of a ranking page.
                type (list[str | None]): The kind of the position: organic, paid, or a SERP feature. Allowed values: `ai_overview`, `ai_overview_sitelink`, `discussion`, `image`, `image_th`, `knowledge_card`, `knowledge_panel`, `local_pack`, `organic`, `organic_shopping`, `paid_top`, `paid_bottom`, `paid_right`, `question`, `sitelink`, `snippet`, `top_story`, `tweet`, `video`, `video_th`.
                update_date (str): The date when we checked search engine results for a keyword.
                nr_words (int | None): The total number of words present in the HTML of a web page.
                domain_rating (float | None): The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale.
                url_rating (float | None): The strength of a page's backlink profile on a 100-point logarithmic scale.
                ahrefs_rank (int | None): The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                backlinks (int | None): The total number of links from other websites pointing to a search result.
                refdomains (int | None): The total number of unique domains linking to a search result.
                traffic (int | None): An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for.
                value (int | None): The estimated value of a page’s monthly organic search traffic, in USD cents.
                keywords (int | None): The total number of keywords that a search result ranks for in the top 100 organic positions.
                top_keyword (str | None): The keyword that brings the most organic traffic to a search result.
                top_keyword_volume (int | None): An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data.
        """
        if request is None:
            _missing = [k for k, v in [("device", device), ("country", country), ("keyword", keyword), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = RankTrackerSerpOverviewRequest(**{k: v for k, v in [("top_positions", top_positions), ("device", device), ("date", date), ("location_id", location_id), ("country", country), ("language_code", language_code), ("keyword", keyword), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("rank-tracker", "serp-overview", request, RankTrackerSerpOverviewResponse, exclude_none=True)

    # Serp Overview API methods
    def serp_overview_serp_overview(
        self,
        request: SerpOverviewSerpOverviewRequest | None = None,
        *,
        select: SelectStr | None = None,
        top_positions: int | None = None,
        date: str | None = None,
        country: CountryEnum | None = None,
        keyword: str | None = None,
    ) -> SerpOverviewSerpOverviewResponse:
        """
        SERP Overview.

        Args:
            request: SerpOverviewSerpOverviewRequest
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                top_positions (int, optional): The number of top organic SERP positions to return. If not specified, all available positions will be returned. Default: None.
                date (str, optional): A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned. Default: None.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                keyword (str, required): The keyword to return SERP Overview for.

        Returns:
            SerpOverviewSerpOverviewResponse containing SerpOverviewSerpOverviewData:
                ahrefs_rank (int | None): The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                backlinks (int | None): The total number of links from other websites pointing to a search result.
                domain_rating (float | None): The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale.
                keywords (int | None): The total number of keywords that a search result ranks for in the top 100 organic positions.
                position (int): The position of the search result in SERP.
                refdomains (int | None): (5 units) The total number of unique domains linking to a search result.
                title (str | None): The title of a ranking page.
                top_keyword (str | None): The keyword that brings the most organic traffic to a search result.
                top_keyword_volume (int | None): (10 units) An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data.
                traffic (int | None): (10 units) An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for.
                type (list[SerpFeaturesItemEnum1 | None]): The kind of the position: organic, paid, or a SERP feature.
                update_date (str): The date when we checked search engine results for a keyword.
                url (str | None): The URL of a ranking page.
                url_rating (float | None): The strength of a page's backlink profile on a 100-point logarithmic scale.
                value (int | None): (10 units) The estimated value of a page’s monthly organic search traffic, in USD cents.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("country", country), ("keyword", keyword)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SerpOverviewSerpOverviewRequest(**{k: v for k, v in [("select", select), ("top_positions", top_positions), ("date", date), ("country", country), ("keyword", keyword)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("serp-overview", "serp-overview", request, SerpOverviewSerpOverviewResponse, exclude_none=True)

    # Site Audit API methods
    def site_audit_issues(
        self,
        request: SiteAuditIssuesRequest | None = None,
        *,
        date_compared: str | None = None,
        date: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditIssuesResponse:
        """
        Project Issues.

        >This endpoint consumes a fixed cost of 50 API units per request.

        Args:
            request: SiteAuditIssuesRequest
                date_compared (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field. Default: None.
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                project_id (int, required): The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`

        Returns:
            SiteAuditIssuesResponse containing SiteAuditIssuesData:
                issue_id (str): The unique identifier of the issue.
                name (str): The name of the issue.
                importance (str): The importance of the issue. Possible values: `Error`, `Warning`, `Notice`.
                category (str): The category of the issue. Possible values: `Internal pages`, `Indexability`, `Links`, `Redirects`, `Content`, `Social tags`, `Duplicates`, `Localization`, `Usability and performance`, `Images`, `JavaScript`, `CSS`, `Sitemaps`, `External pages`, `Other`.
                is_indexable (bool | None): True if the issue applies only to indexable pages.
                crawled (int): Number of URLs currently affected by the issue.
                change (int | None): Difference in the number of affected URLs between the specified dates.
                added (int | None): Number of URLs that have the issue on the current date but did not have it on the previous date.
                new (int | None): Number of newly discovered URLs that have the issue on the current date.
                removed (int | None): Number of URLs that had the issue on the previous date but no longer have it on the current date.
                missing (int | None): Number of URLs that had the issue on the previous date but cannot be found on the current date.
        """
        if request is None:
            _missing = [k for k, v in [("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteAuditIssuesRequest(**{k: v for k, v in [("date_compared", date_compared), ("date", date), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-audit", "issues", request, SiteAuditIssuesResponse, exclude_none=True)

    def site_audit_page_content(
        self,
        request: SiteAuditPageContentRequest | None = None,
        *,
        select: SelectStr | None = None,
        date: str | None = None,
        target_url: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditPageContentResponse:
        """
        Page content.

        >This endpoint consumes a fixed cost of 50 API units per request.

        Args:
            request: SiteAuditPageContentRequest
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                target_url (str, required): The URL of the page to retrieve content for.
                project_id (int, required): The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`

        Returns:
            SiteAuditPageContentResponse containing SiteAuditPageContentData:
                crawl_datetime (str): The timestamp when the page was crawled.
                page_text (str | None): The text extracted from the page content.
                raw_html (str | None): The raw HTML of the page.
                rendered_html (str | None): The rendered HTML of the page.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target_url", target_url), ("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteAuditPageContentRequest(**{k: v for k, v in [("select", select), ("date", date), ("target_url", target_url), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-audit", "page-content", request, SiteAuditPageContentResponse, exclude_none=True)

    def site_audit_page_explorer(
        self,
        request: SiteAuditPageExplorerRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        filter_mode: FilterModeEnum | None = None,
        issue_id: str | None = None,
        date_compared: str | None = None,
        date: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditPageExplorerResponse:
        """
        Page explorer.

        >This endpoint consumes a fixed cost of 50 API units per request.

        Args:
            request: SiteAuditPageExplorerRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'page_rating,url,is_rendered,http_code,content_type,title,meta_description,h1,traffic,canonical,canonical_code,redirect,redirect_code,compliant,page_is_noindex,page_is_nofollow,incoming_all_links,links_count_internal,links_count_external,links_count_internal4xx,links_count_external4xx,hreflang_issues,psi_crux_cls_category,psi_crux_lcp_category,psi_crux_inp_category,jsonld_schema_types,jsonld_validation_kinds,origin,depth'.
                filter_mode (FilterModeEnum, optional): Indicates which pages to return compared to the previous crawl. If not specified, all URLs that match your filter conditions are returned. `added`: URLs that are a new match for your filter conditions. `new`: URLs that are newly crawled and match your filter conditions. `removed`: URLs that stopped matching your filter conditions. `missing`: URLs that weren't crawled, but previously matched your filter conditions. `no_change`: URLs that match your filter conditions in a crawl and the crawl before it. Default: None.
                issue_id (str, optional): The unique identifier of an issue. When specified, only URLs affected by this issue are returned. You can get issue IDs by querying the `site-audit/issues` endpoint. Default: None.
                date_compared (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field. Default: None.
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                project_id (int, required): The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`

        Returns:
            SiteAuditPageExplorerResponse containing SiteAuditPageExplorerData:
                ai_content_level (str | None): The estimated percentage of AI-generated text on the page. Possible values: `None`, `Low`, `Moderate`, `High`, `Very High`
                ai_content_status (str | None): AI detection status for each page. Possible values: - `Success`: Content analyzed successfully - `Content_too_short`: Not enough text for reliable detection - `Not_eligible`: URL isn't an internal HTML page - `Failed`: Internal issue prevented detection - `Detection_off`: Disabled in Crawl settings
                alternate (int | None): The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database)
                alternate_diff (int | None): The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database)
                alternate_prev (int | None): The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database)
                backlinks (int | None): The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                backlinks_diff (int | None): The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                backlinks_prev (int | None): The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical (str | None): The URL of the canonical version of the page
                canonical_code (int | None): The HTTP status code of the canonical URL
                canonical_counts (int | None): The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical_counts_diff (int | None): The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical_counts_prev (int | None): The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks
                canonical_group_hash (int | None): The ID of the group of pages that have the same canonical URL
                canonical_is_canonical (bool | None): Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical
                canonical_is_canonical_prev (bool | None): Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical
                canonical_no_crawl_reason (str | None): The reason why the canonical version of the page was not crawled
                canonical_no_crawl_reason_prev (str | None): The reason why the canonical version of the page was not crawled
                canonical_prev (str | None): The URL of the canonical version of the page
                canonical_scheme (str | None): The protocol of the canonical URL
                canonical_scheme_prev (str | None): The protocol of the canonical URL
                compliant (bool | None): Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the "rel=canonical" tag pointing to a different URL nor the "noindex" directive
                compliant_prev (bool | None): Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the "rel=canonical" tag pointing to a different URL nor the "noindex" directive
                compression (str | None): The data compression scheme
                compression_prev (str | None): The data compression scheme
                content_encoding (str | None): The Content-Encoding HTTP response header field
                content_encoding_prev (str | None): The Content-Encoding HTTP response header field
                content_length (int | None): The character length of content displayed on the page
                content_length_diff (int | None): The character length of content displayed on the page
                content_length_prev (int | None): The character length of content displayed on the page
                ... and 575 more fields. See SiteAuditPageExplorerData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("project_id", project_id)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteAuditPageExplorerRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("filter_mode", filter_mode), ("issue_id", issue_id), ("date_compared", date_compared), ("date", date), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-audit", "page-explorer", request, SiteAuditPageExplorerResponse, exclude_none=True)

    def site_audit_projects(
        self,
        request: SiteAuditProjectsRequest | None = None,
        *,
        date: str | None = None,
        project_id: int | None = None,
    ) -> SiteAuditProjectsResponse:
        """
        Project Health Scores.

        >Requests to this endpoint are free and do not consume any API units.

        Args:
            request: SiteAuditProjectsRequest
                date (str, optional): A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. Default: None.
                project_id (int, optional): The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#` Default: None.

        Returns:
            SiteAuditProjectsResponse containing SiteAuditProjectsData:
                project_id (str): The unique identifier of the project.
                project_name (str): The project name.
                target_protocol (str): The protocol of the target. Possible values: `both`, `http`, `https`.
                target_url (str): The URL of the project's target.
                target_mode (str): The scope of the target. Possible values: `exact`, `prefix`, `domain`, `subdomains`.
                date (str | None): The finish date and time of the last finished crawl, in GMT time zone.
                status (str | None): The status of the most recent finished crawl. Possible values: `Completed`, `Stopped`, `Error`, `In_progress`.
                health_score (int | None): Reflects the proportion of internal URLs on your site that do not have errors, based on the last finished crawl. Excludes crawls that are starting, in progress, finalizing, or were skipped.
                urls_with_errors (int | None): Number of internal URLs with errors
                urls_with_warnings (int | None): Number of internal URLs with warnings
                urls_with_notices (int | None): Number of internal URLs with notices
                total (int | None): Number of total crawled internal URLs
        """
        if request is None:
            request = SiteAuditProjectsRequest(**{k: v for k, v in [("date", date), ("project_id", project_id)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-audit", "projects", request, SiteAuditProjectsResponse, exclude_none=True)

    # Site Explorer API methods
    def site_explorer_all_backlinks(
        self,
        request: SiteExplorerAllBacklinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        aggregation: AggregationEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerAllBacklinksResponse:
        """
        Backlinks.

        Args:
            request: SiteExplorerAllBacklinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `link_group_count`, which is not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                aggregation (AggregationEnum, optional): The backlinks grouping mode. Default: 'similar_links'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerAllBacklinksResponse containing SiteExplorerAllBacklinksData:
                ahrefs_rank_source (int): The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                ahrefs_rank_target (int): The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                alt (str | None): The alt attribute of the link.
                anchor (str): The clickable words in a link that point to a URL.
                broken_redirect_new_target (str | None): The new destination of a modified redirect.
                broken_redirect_reason (BrokenRedirectReasonEnum | None): The reason the redirect was considered broken during the last crawl.
                broken_redirect_source (str | None): The redirecting URL that was modified, causing the redirect to become broken.
                class_c (int): (5 units) The number of unique class_c subnets linking to the referring page.
                discovered_status (DiscoveredStatusEnum | None): The reason the link was discovered during the last crawl: the page was crawled for the first time, the link was added to the page, or the link re-appeared after being removed.
                domain_rating_source (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                domain_rating_target (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                drop_reason (DropReasonEnum | None): The reason we removed the link from our index.
                encoding (str): The character set encoding of the referring page HTML.
                first_seen (str): The date the referring page URL was first discovered.
                first_seen_link (str): The date we first found a backlink to your target on a given referring page.
                http_code (int): The return code from HTTP protocol returned during the referring page crawl.
                http_crawl (bool): The link was discovered without executing javascript and rendering the page.
                ip_source (str | None): The referring domain IP address.
                is_alternate (bool): The link with the rel=“alternate” attribute.
                is_canonical (bool): The link with the rel=“canonical” attribute.
                is_content (bool): The link was found in the biggest piece of content on the page.
                is_dofollow (bool): The link has no special nofollow attribute.
                is_form (bool): The link was found in a form HTML tag.
                is_frame (bool): The link was found in an iframe HTML tag.
                is_image (bool): The link is a regular link that has an image inside their href attribute.
                is_lost (bool): The link currently does not exist anymore.
                is_new (bool): The link was discovered on the last crawl.
                is_nofollow (bool): The link or the referring page has the nofollow attribute set.
                is_redirect (bool): The link pointing to your target via a redirect.
                is_redirect_lost (bool): The redirected link currently does not exist anymore.
                ... and 50 more fields. See SiteExplorerAllBacklinksData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerAllBacklinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("aggregation", aggregation), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "all-backlinks", request, SiteExplorerAllBacklinksResponse, exclude_none=True)

    def site_explorer_anchors(
        self,
        request: SiteExplorerAnchorsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerAnchorsResponse:
        """
        Anchors.

        Args:
            request: SiteExplorerAnchorsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerAnchorsResponse containing SiteExplorerAnchorsData:
                anchor (str): The clickable words in a link that point to a URL.
                dofollow_links (int): The number of links with a given anchor to your target that don’t have the “nofollow” attribute.
                first_seen (str): The date we first found a link with a given anchor to your target.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                last_seen (str | None): The date we discovered the last backlink with a given anchor was lost.
                links_to_target (int): The number of inbound backlinks your target has with a given anchor.
                lost_links (int): The number of backlinks with a given anchor lost during the selected time period.
                new_links (int): The number of new backlinks with a given anchor found during the selected time period.
                refdomains (int): (5 units) The number of unique domains linking to your target with a given anchor.
                refpages (int): The number of pages containing a link with a given anchor to your target.
                top_domain_rating (float): The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerAnchorsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "anchors", request, SiteExplorerAnchorsResponse, exclude_none=True)

    def site_explorer_backlinks_stats(
        self,
        request: SiteExplorerBacklinksStatsRequest | None = None,
        *,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerBacklinksStatsResponse:
        """
        Backlinks stats.

        Args:
            request: SiteExplorerBacklinksStatsRequest
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerBacklinksStatsResponse containing SiteExplorerBacklinksStatsData:
                live (int): The total number of links from other websites pointing to your target.
                all_time (int): The total number of links from other websites pointing to your target for all time.
                live_refdomains (int): (5 units) The total number of unique domains linking to your target.
                all_time_refdomains (int): (5 units) The total number of unique domains linking to your target for all time.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBacklinksStatsRequest(**{k: v for k, v in [("protocol", protocol), ("target", target), ("mode", mode), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "backlinks-stats", request, SiteExplorerBacklinksStatsResponse, exclude_none=True)

    def site_explorer_best_by_external_links(
        self,
        request: SiteExplorerBestByExternalLinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerBestByExternalLinksResponse:
        """
        Best by External Links.

        Args:
            request: SiteExplorerBestByExternalLinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `http_code_target`, `languages_target`, `last_visited_target`, `powered_by_target`, `target_redirect`, `title_target`, `url_rating_target`, which are not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerBestByExternalLinksResponse containing SiteExplorerBestByExternalLinksData:
                dofollow_to_target (int): The number of links to your target page that don’t have the “nofollow” attribute.
                first_seen_link (str): The date we first found a link to your target.
                http_code_target (int | None): The return code from HTTP protocol returned during the target page crawl.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                languages_target (list[str | None]): The languages listed in the target page metadata or detected by the crawler to appear in the HTML.
                last_seen (str | None): The date your target page lost its last live link.
                last_visited_source (str): The date we last verified a live link to your target page.
                last_visited_target (str | None): The date we last crawled your target page.
                links_to_target (int): The number of inbound backlinks the target page has.
                lost_links_to_target (int): The number of backlinks lost during the selected time period.
                new_links_to_target (int): The number of new backlinks found during the selected time period.
                nofollow_to_target (int): The number of links to your target page that have the “nofollow” attribute.
                powered_by_target (list[str | None]): Web technologies used to build and serve the target page content.
                redirects_to_target (int): The number of inbound redirects to your target page.
                refdomains_target (int): (5 units) The number of unique referring domains linking to the target page.
                target_redirect (str | None): The target's redirect if any.
                title_target (str | None): The html title of the target page.
                top_domain_rating_source (float): The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.
                url_rating_target (float | None): The strength of the target page's backlink profile compared to the others in our database on a 100-point scale.
                url_to (str): The URL the backlink points to.
                url_to_plain (str): The target page URL optimized for use as a filter.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBestByExternalLinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "best-by-external-links", request, SiteExplorerBestByExternalLinksResponse, exclude_none=True)

    def site_explorer_best_by_internal_links(
        self,
        request: SiteExplorerBestByInternalLinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerBestByInternalLinksResponse:
        """
        Best by Internal Links.

        Args:
            request: SiteExplorerBestByInternalLinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerBestByInternalLinksResponse containing SiteExplorerBestByInternalLinksData:
                canonical_to_target (int): The number of inbound canonical links to your target page.
                dofollow_to_target (int): The number of links to your target page that don’t have the “nofollow” attribute.
                first_seen_link (str): The date we first found a link to your target.
                http_code_target (int | None): The return code from HTTP protocol returned during the target page crawl.
                languages_target (list[str | None]): The languages listed in the target page metadata or detected by the crawler to appear in the HTML.
                last_seen (str | None): The date your target page lost its last live link.
                last_visited_source (str): The date we last verified a live link to your target page.
                last_visited_target (str | None): The date we last crawled your target page.
                links_to_target (int): The number of inbound backlinks the target page has.
                nofollow_to_target (int): The number of links to your target page that have the “nofollow” attribute.
                powered_by_target (list[str | None]): Web technologies used to build and serve the target page content.
                redirects_to_target (int): The number of inbound redirects to your target page.
                target_redirect (str | None): The target's redirect if any.
                title_target (str | None): The html title of the target page.
                url_rating_target (float | None): The strength of the target page's backlink profile compared to the others in our database on a 100-point scale.
                url_to (str): The URL the backlink points to.
                url_to_plain (str): The target page URL optimized for use as a filter.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBestByInternalLinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "best-by-internal-links", request, SiteExplorerBestByInternalLinksResponse, exclude_none=True)

    def site_explorer_broken_backlinks(
        self,
        request: SiteExplorerBrokenBacklinksRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        aggregation: AggregationEnum | None = None,
    ) -> SiteExplorerBrokenBacklinksResponse:
        """
        Broken Backlinks.

        Args:
            request: SiteExplorerBrokenBacklinksRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See the response schema for valid column identifiers, except for `link_group_count`, `last_visited_target`, `http_code_target`, which are not supported in `order_by` for this endpoint. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                aggregation (AggregationEnum, optional): The backlinks grouping mode. Default: 'similar_links'.

        Returns:
            SiteExplorerBrokenBacklinksResponse containing SiteExplorerBrokenBacklinksData:
                ahrefs_rank_source (int): The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                ahrefs_rank_target (int): The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
                alt (str | None): The alt attribute of the link.
                anchor (str): The clickable words in a link that point to a URL.
                class_c (int): (5 units) The number of unique class_c subnets linking to the referring page.
                domain_rating_source (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                domain_rating_target (float): The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.
                encoding (str): The character set encoding of the referring page HTML.
                first_seen (str): The date the referring page URL was first discovered.
                first_seen_link (str): The date we first found a backlink to your target on a given referring page.
                http_code (int): The return code from HTTP protocol returned during the referring page crawl.
                http_code_target (int | None): The return code from HTTP protocol returned during the target page crawl.
                http_crawl (bool): The link was discovered without executing javascript and rendering the page.
                ip_source (str | None): The referring domain IP address.
                is_alternate (bool): The link with the rel=“alternate” attribute.
                is_canonical (bool): The link with the rel=“canonical” attribute.
                is_content (bool): The link was found in the biggest piece of content on the page.
                is_dofollow (bool): The link has no special nofollow attribute.
                is_form (bool): The link was found in a form HTML tag.
                is_frame (bool): The link was found in an iframe HTML tag.
                is_image (bool): The link is a regular link that has an image inside their href attribute.
                is_nofollow (bool): The link or the referring page has the nofollow attribute set.
                is_redirect (bool): The link pointing to your target via a redirect.
                is_root_source (bool): The referring domain name is a root domain name.
                is_root_target (bool): The target domain name is a root domain name.
                is_rss (bool): The link was found in an RSS feed.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                is_sponsored (bool): The link has the Sponsored attribute set in the referring page HTML.
                is_text (bool): The link is a standard href hyperlink.
                is_ugc (bool): The link has the User Generated Content attribute set in the referring page HTML.
                ... and 41 more fields. See SiteExplorerBrokenBacklinksData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerBrokenBacklinksRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("aggregation", aggregation)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "broken-backlinks", request, SiteExplorerBrokenBacklinksResponse, exclude_none=True)

    def site_explorer_domain_rating(
        self,
        request: SiteExplorerDomainRatingRequest | None = None,
        *,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerDomainRatingResponse:
        """
        Domain rating.

        Args:
            request: SiteExplorerDomainRatingRequest
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerDomainRatingResponse containing SiteExplorerDomainRatingData:
                domain_rating (float): The strength of your target's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.
                ahrefs_rank (int | None): The strength of your target's backlink profile compared to the other websites in our database, with rank #1 being the strongest.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerDomainRatingRequest(**{k: v for k, v in [("protocol", protocol), ("target", target), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "domain-rating", request, SiteExplorerDomainRatingResponse, exclude_none=True)

    def site_explorer_domain_rating_history(
        self,
        request: SiteExplorerDomainRatingHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        target: str | None = None,
    ) -> SiteExplorerDomainRatingHistoryResponse:
        """
        Domain Rating history.

        Args:
            request: SiteExplorerDomainRatingHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                target (str, required): The target of the search: a domain or a URL.

        Returns:
            SiteExplorerDomainRatingHistoryResponse containing SiteExplorerDomainRatingHistoryData:
                date (str)
                domain_rating (float): The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerDomainRatingHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("target", target)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "domain-rating-history", request, SiteExplorerDomainRatingHistoryResponse, exclude_none=True)

    def site_explorer_keywords_history(
        self,
        request: SiteExplorerKeywordsHistoryRequest | None = None,
        *,
        select: SelectStr | None = None,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerKeywordsHistoryResponse:
        """
        Keywords history.

        Args:
            request: SiteExplorerKeywordsHistoryRequest
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'date,top3,top4_10,top11_plus'.
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerKeywordsHistoryResponse containing SiteExplorerKeywordsHistoryData:
                date (str)
                top11_20 (int): The total number of keywords that your target ranks for in the top 11-20 organic search results.
                top11_plus (int): The total number of keywords that your target ranks for in the top 11+ organic search results.
                top21_50 (int): The total number of keywords that your target ranks for in the top 21-50 organic search results.
                top3 (int): The total number of keywords that your target ranks for in the top 3 organic search results.
                top4_10 (int): The total number of keywords that your target ranks for in the top 4-10 organic search results.
                top51_plus (int): The total number of keywords that your target ranks for in the top 51+ organic search results.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerKeywordsHistoryRequest(**{k: v for k, v in [("select", select), ("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "keywords-history", request, SiteExplorerKeywordsHistoryResponse, exclude_none=True)

    def site_explorer_linked_anchors_external(
        self,
        request: SiteExplorerLinkedAnchorsExternalRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerLinkedAnchorsExternalResponse:
        """
        Outgoing external anchors.

        Args:
            request: SiteExplorerLinkedAnchorsExternalRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerLinkedAnchorsExternalResponse containing SiteExplorerLinkedAnchorsExternalData:
                anchor (str): The clickable words in a link that point to a URL.
                dofollow_links (int): The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute.
                first_seen (str): The date we first found a link with a given anchor on your target.
                linked_domains (int): The number of unique domains linked from your target with a given anchor.
                linked_pages (int): The number of unique pages linked from your target with a given anchor.
                links_from_target (int): The number of outbound links your target has with a given anchor.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerLinkedAnchorsExternalRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "linked-anchors-external", request, SiteExplorerLinkedAnchorsExternalResponse, exclude_none=True)

    def site_explorer_linked_anchors_internal(
        self,
        request: SiteExplorerLinkedAnchorsInternalRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerLinkedAnchorsInternalResponse:
        """
        Outgoing internal anchors.

        Args:
            request: SiteExplorerLinkedAnchorsInternalRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerLinkedAnchorsInternalResponse containing SiteExplorerLinkedAnchorsInternalData:
                anchor (str): The clickable words in a link that point to a URL.
                dofollow_links (int): The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute.
                first_seen (str): The date we first found a link with a given anchor on your target.
                linked_pages (int): The number of unique pages linked from your target with a given anchor.
                links_from_target (int): The number of outbound links your target has with a given anchor.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerLinkedAnchorsInternalRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "linked-anchors-internal", request, SiteExplorerLinkedAnchorsInternalResponse, exclude_none=True)

    def site_explorer_linkeddomains(
        self,
        request: SiteExplorerLinkeddomainsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerLinkeddomainsResponse:
        """
        Linked Domains.

        Args:
            request: SiteExplorerLinkeddomainsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerLinkeddomainsResponse containing SiteExplorerLinkeddomainsData:
                dofollow_linked_domains (int): The number of unique root domains with dofollow links linked from the linked domain.
                dofollow_links (int): The number of links from your target to the linked domain that don’t have the “nofollow” attribute.
                dofollow_refdomains (int): (5 units) The number of unique domains with dofollow links to the linked domain.
                domain (str): A linked domain that has at least one link from your target.
                domain_rating (float): The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.
                first_seen (str): The date we first found a link to the linked domain from your target.
                is_root_domain (bool): The domain name is a root domain name.
                linked_domain_traffic (int): (10 units) The linked domain’s estimated monthly organic traffic from search
                linked_pages (int): The number of the domain's pages linked from your target.
                links_from_target (int): The number of links to the linked domain from your target.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerLinkeddomainsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "linkeddomains", request, SiteExplorerLinkeddomainsResponse, exclude_none=True)

    def site_explorer_metrics(
        self,
        request: SiteExplorerMetricsRequest | None = None,
        *,
        volume_mode: VolumeModeEnum | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerMetricsResponse:
        """
        Metrics.

        Args:
            request: SiteExplorerMetricsRequest
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerMetricsResponse containing SiteExplorerMetricsData:
                org_keywords (int): The total number of keywords that your target ranks for in the top 100 organic search results.
                paid_keywords (int): The total number of keywords that your target ranks for in paid search results.
                org_keywords_1_3 (int): The total number of keywords that your target ranks for in the top 3 organic search results.
                org_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from organic search.
                org_cost (int | None): (10 units) The estimated value of your target's monthly organic search traffic, in USD cents.
                paid_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from paid search.
                paid_cost (int | None): (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.
                paid_pages (int): The total number of pages from a target ranking in paid search results.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerMetricsRequest(**{k: v for k, v in [("volume_mode", volume_mode), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "metrics", request, SiteExplorerMetricsResponse, exclude_none=True)

    def site_explorer_metrics_by_country(
        self,
        request: SiteExplorerMetricsByCountryRequest | None = None,
        *,
        select: SelectStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        date: DateStr | None = None,
    ) -> SiteExplorerMetricsByCountryResponse:
        """
        Metrics by country.

        Args:
            request: SiteExplorerMetricsByCountryRequest
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'paid_cost,paid_keywords,org_cost,paid_pages,org_keywords_1_3,org_keywords,org_traffic,paid_traffic,country'.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.

        Returns:
            SiteExplorerMetricsByCountryResponse containing SiteExplorerMetricsByCountryData:
                country (CountryEnum1)
                org_cost (int | None): (10 units) The estimated value of your target's monthly organic search traffic, in USD cents.
                org_keywords (int): The total number of keywords that your target ranks for in the top 100 organic search results.
                org_keywords_1_3 (int): The total number of keywords that your target ranks for in the top 3 organic search results.
                org_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from organic search.
                paid_cost (int | None): (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.
                paid_keywords (int): The total number of keywords that your target ranks for in paid search results.
                paid_pages (int): The total number of pages from a target ranking in the top 100 paid search results.
                paid_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from paid search.
        """
        if request is None:
            _missing = [k for k, v in [("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerMetricsByCountryRequest(**{k: v for k, v in [("select", select), ("volume_mode", volume_mode), ("protocol", protocol), ("target", target), ("mode", mode), ("date", date)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "metrics-by-country", request, SiteExplorerMetricsByCountryResponse, exclude_none=True)

    def site_explorer_metrics_history(
        self,
        request: SiteExplorerMetricsHistoryRequest | None = None,
        *,
        select: SelectStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerMetricsHistoryResponse:
        """
        Metrics history.

        Args:
            request: SiteExplorerMetricsHistoryRequest
                select (str, optional): A comma-separated list of columns to return. See response schema for valid column identifiers. Default: 'date,org_cost,org_traffic,paid_cost,paid_traffic'.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerMetricsHistoryResponse containing SiteExplorerMetricsHistoryData:
                date (str)
                org_cost (int): (10 units) The estimated cost of your target's monthly organic search traffic, in USD cents.
                org_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from organic search.
                paid_cost (int): (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.
                paid_traffic (int): (10 units) The estimated number of monthly visitors that your target gets from paid search.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerMetricsHistoryRequest(**{k: v for k, v in [("select", select), ("volume_mode", volume_mode), ("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "metrics-history", request, SiteExplorerMetricsHistoryResponse, exclude_none=True)

    def site_explorer_organic_competitors(
        self,
        request: SiteExplorerOrganicCompetitorsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerOrganicCompetitorsResponse:
        """
        Organic competitors.

        Args:
            request: SiteExplorerOrganicCompetitorsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, required): A two-letter country code (ISO 3166-1 alpha-2).
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerOrganicCompetitorsResponse containing SiteExplorerOrganicCompetitorsData:
                competitor_domain (str | None): A competitor's domain of your target in “domains" group mode.
                competitor_url (str | None): A competitor's URL of your target in pages" group mode.
                domain_rating (float): The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.
                group_mode (GroupModeEnum): To see competing pages instead, use the “exact URL” target mode or “path” target mode if your target doesn't have multiple pages.
                keywords_common (int): Organic keywords that both your target and a competitor are ranking for.
                keywords_competitor (int): Organic keywords that a competitor is ranking for, but your target isn't.
                keywords_target (int): Organic keywords that your target is ranking for, but a competitor isn't.
                pages (int | None): The total number of pages from a target ranking in search results.
                pages_diff (int): The change in pages between your selected dates.
                pages_merged (int): The pages field optimized for sorting.
                pages_prev (int | None): The total number of pages from a target ranking in search results on the comparison date.
                share (float): The percentage of common keywords out of the total number of keywords that your target and a competitor both rank for.
                traffic (int | None): (10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
                traffic_diff (int): The change in traffic between your selected dates.
                traffic_merged (int): (10 units) The traffic field optimized for sorting.
                traffic_prev (int | None): (10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter on the comparison date.
                value (int | None): (10 units) The estimated value of a page's monthly organic search traffic, in USD cents.
                value_diff (int): The change in value between your selected dates.
                value_merged (int | None): (10 units) The value field optimized for sorting.
                value_prev (int | None): (10 units) The estimated value of a page's monthly organic search traffic, in USD cents on the comparison date.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("country", country), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerOrganicCompetitorsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "organic-competitors", request, SiteExplorerOrganicCompetitorsResponse, exclude_none=True)

    def site_explorer_organic_keywords(
        self,
        request: SiteExplorerOrganicKeywordsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerOrganicKeywordsResponse:
        """
        Organic keywords.

        Args:
            request: SiteExplorerOrganicKeywordsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerOrganicKeywordsResponse containing SiteExplorerOrganicKeywordsData:
                all_positions (list[dict[str, Any] | None]): (5 units) The list of all positions for a keyword.
                all_positions_prev (list[dict[str, Any] | None]): (5 units) The list of all positions for a keyword on the comparison date.
                best_position (int | None): The top position your target ranks for in the organic search results for a keyword.
                best_position_diff (int | None): The change in position between your selected dates.
                best_position_has_thumbnail (bool | None): The top position has a thumbnail.
                best_position_has_thumbnail_prev (bool | None): The top position has a thumbnail on the comparison date.
                best_position_has_video (bool | None): The top position has a video.
                best_position_has_video_prev (bool | None): The top position has a video on the comparison date.
                best_position_kind (BestPositionKindEnum | None): The kind of the top position: organic, paid, or a SERP feature.
                best_position_kind_merged (BestPositionKindEnum): The kind of the top position optimized for sorting.
                best_position_kind_prev (BestPositionKindEnum | None): The kind of the top position on the comparison date.
                best_position_prev (int | None): The top position on the comparison date.
                best_position_set (BestPositionSetEnum): The ranking group of the top position.
                best_position_set_prev (BestPositionSetEnum | None): The ranking group of the top position on the comparison date.
                best_position_url (str | None): The ranking URL in organic search results.
                best_position_url_prev (str | None): The ranking URL on the comparison date.
                cpc (int | None): Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.
                cpc_merged (int | None): The CPC field optimized for sorting.
                cpc_prev (int | None): The CPC metric on the comparison date.
                entities (list[dict[str, Any] | None]): Organizations, products, persons, works, events, and locations found in a keyword.
                is_best_position_set_top_11_50 (bool): The ranking group of the top position is 11-50.
                is_best_position_set_top_11_50_prev (bool | None): The ranking group of the top position was 11-50 on the comparison date.
                is_best_position_set_top_3 (bool): The ranking group of the top position is Top 3.
                is_best_position_set_top_3_prev (bool | None): The ranking group of the top position was Top 3 on the comparison date.
                is_best_position_set_top_4_10 (bool): The ranking group of the top position is 4-10.
                is_best_position_set_top_4_10_prev (bool | None): The ranking group of the top position was 4-10 on the comparison date.
                is_branded (bool): User intent: branded. The user is searching for a specific brand or company name.
                is_commercial (bool): User intent: commercial. The user is comparing products or services before making a purchase decision.
                is_informational (bool): User intent: informational. The user is looking for information or an answer to a specific question.
                is_local (bool): User intent: local. The user is looking for information relevant to a specific location or nearby services.
                ... and 37 more fields. See SiteExplorerOrganicKeywordsData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerOrganicKeywordsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "organic-keywords", request, SiteExplorerOrganicKeywordsResponse, exclude_none=True)

    def site_explorer_outlinks_stats(
        self,
        request: SiteExplorerOutlinksStatsRequest | None = None,
        *,
        protocol: ProtocolEnum | None = None,
        mode: ModeEnum | None = None,
        target: str | None = None,
    ) -> SiteExplorerOutlinksStatsResponse:
        """
        Outlinks stats.

        **This is a beta version of the endpoint. The data it returns may not always exactly match the corresponding values in Ahrefs UI. Data accuracy will be improved soon.**

        Args:
            request: SiteExplorerOutlinksStatsRequest
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                target (str, required): The target of the search: a domain or a URL.

        Returns:
            SiteExplorerOutlinksStatsResponse containing SiteExplorerOutlinksStatsData:
                outgoing_links (int): The number of external links from the target.
                outgoing_links_dofollow (int): The number of external dofollow links from the target.
                linked_domains (int): The number of unique root domains linked from the target.
                linked_domains_dofollow (int): The number of unique root domains linked via dofollow links from the target.
        """
        if request is None:
            _missing = [k for k, v in [("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerOutlinksStatsRequest(**{k: v for k, v in [("protocol", protocol), ("mode", mode), ("target", target)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "outlinks-stats", request, SiteExplorerOutlinksStatsResponse, exclude_none=True)

    def site_explorer_pages_by_traffic(
        self,
        request: SiteExplorerPagesByTrafficRequest | None = None,
        *,
        volume_mode: VolumeModeEnum | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerPagesByTrafficResponse:
        """
        Pages by traffic.

        Args:
            request: SiteExplorerPagesByTrafficRequest
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerPagesByTrafficResponse containing SiteExplorerPagesByTrafficData:
                range0_pages (int): The total number of pages with 0 traffic.
                range100_traffic (int): (10 units) The total traffic from pages with 1-100 traffic.
                range100_pages (int): The total number of pages with 1-100 traffic.
                range1k_traffic (int): (10 units) The total traffic from pages with 101-1K traffic.
                range1k_pages (int): The total number of pages with 101-1K traffic.
                range5k_traffic (int): (10 units) The total traffic from pages with 1K-5K traffic.
                range5k_pages (int): The total number of pages with 1K-5K traffic.
                range10k_traffic (int): (10 units) The total traffic from pages with 5K-10K traffic.
                range10k_pages (int): The total number of pages with 5K-10K traffic.
                range10k_plus_traffic (int): (10 units) The total traffic from pages with 10K+ traffic.
                range10k_plus_pages (int): The total number of pages with 10K+ traffic.
        """
        if request is None:
            _missing = [k for k, v in [("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerPagesByTrafficRequest(**{k: v for k, v in [("volume_mode", volume_mode), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "pages-by-traffic", request, SiteExplorerPagesByTrafficResponse, exclude_none=True)

    def site_explorer_pages_history(
        self,
        request: SiteExplorerPagesHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerPagesHistoryResponse:
        """
        Pages history.

        Args:
            request: SiteExplorerPagesHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerPagesHistoryResponse containing SiteExplorerPagesHistoryData:
                date (str)
                pages (int): The total number of pages from a target ranking in the top 100 organic search results.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerPagesHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "pages-history", request, SiteExplorerPagesHistoryResponse, exclude_none=True)

    def site_explorer_paid_pages(
        self,
        request: SiteExplorerPaidPagesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerPaidPagesResponse:
        """
        Paid pages.

        Args:
            request: SiteExplorerPaidPagesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerPaidPagesResponse containing SiteExplorerPaidPagesData:
                ads_count (int | None): The number of unique ads with a page.
                ads_count_diff (int): The change in ads between your selected dates.
                ads_count_prev (int | None): The number of ads on the comparison date.
                keywords (int | None): The total number of keywords that your target ranks for in paid search results.
                keywords_diff (int): The change in keywords between your selected dates.
                keywords_diff_percent (int): The change in keywords between your selected dates, in percents.
                keywords_merged (int): The total number of keywords optimized for sorting.
                keywords_prev (int | None): The keyword your target ranks for on the comparison date.
                raw_url (str): The ranking page URL in encoded format.
                raw_url_prev (str | None): The ranking page URL on the comparison date in encoded format.
                referring_domains (int | None): (5 units) The number of unique domains linking to a page.
                status (StatusEnum): The status of a page: the new page that just started to rank in paid results ("left"), the lost page that disappeared from paid results ("right"), or no change ("both").
                sum_traffic (int | None): (10 units) An estimation of the monthly paid search traffic that a page gets from all the keywords that it ranks for.
                sum_traffic_merged (int): (10 units) The paid traffic field optimized for sorting.
                sum_traffic_prev (int | None): (10 units) The paid traffic on the comparison date.
                top_keyword (str | None): The keyword that brings the most paid traffic to a page.
                top_keyword_best_position (int | None): The ranking position that a page holds for its top keyword.
                top_keyword_best_position_diff (int | None): The change in the top position between your selected dates.
                top_keyword_best_position_kind (BestPositionKindEnum | None): The kind of the top position: organic, paid or a SERP feature.
                top_keyword_best_position_kind_prev (BestPositionKindEnum | None): The kind of the top position on the comparison date.
                top_keyword_best_position_prev (int | None): The top position on the comparison date.
                top_keyword_best_position_title (str | None): The title displayed for the page in its top keyword's SERP.
                top_keyword_best_position_title_prev (str | None): The title displayed for the page in its top keyword's SERP on the comparison date.
                top_keyword_country (CountryEnum1 | None): The country in which a page ranks for its top keyword.
                top_keyword_country_prev (CountryEnum1 | None): The country in which a page ranks for its top keyword on the comparison date.
                top_keyword_prev (str | None): The keyword that brings the most paid traffic to a page on the comparison date.
                top_keyword_volume (int | None): (10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
                top_keyword_volume_prev (int | None): (10 units) The search volume on the comparison date.
                traffic_diff (int): The change in traffic between your selected dates.
                traffic_diff_percent (int): The change in traffic between your selected dates, in percents.
                ... and 8 more fields. See SiteExplorerPaidPagesData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerPaidPagesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "paid-pages", request, SiteExplorerPaidPagesResponse, exclude_none=True)

    def site_explorer_refdomains(
        self,
        request: SiteExplorerRefdomainsRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        history: str | None = None,
    ) -> SiteExplorerRefdomainsResponse:
        """
        Refdomains.

        Args:
            request: SiteExplorerRefdomainsRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                history (str, optional): A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. Default: 'all_time'.

        Returns:
            SiteExplorerRefdomainsResponse containing SiteExplorerRefdomainsData:
                dofollow_linked_domains (int): The number of unique root domains with dofollow links linked from the referring domain.
                dofollow_links (int): The number of links from the referring domain to your target that don't have the “nofollow” attribute.
                dofollow_refdomains (int): (5 units) The number of unique domains with dofollow links to the referring domain.
                domain (str): A referring domain that has at least one link to your target.
                domain_rating (float): The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.
                first_seen (str): The date we first found a backlink to your target from the referring domain.
                ip_source (str | None): The referring domain IP address.
                is_root_domain (bool): The domain name is a root domain name.
                is_spam (bool): Indicates whether the backlink comes from a known spammy domain.
                last_seen (str | None): The date your target lost its last live backlink for the referring domain.
                links_to_target (int): The number of backlinks from the referring domain to your target.
                lost_links (int): The number of backlinks lost from the referring domain for the selected time period.
                new_links (int): The number of new backlinks found from the referring domain for the selected time period.
                positions_source_domain (int): The number of keywords that the referring domain ranks for in the top 100 positions.
                traffic_domain (int): (10 units) The referring domain's estimated monthly organic traffic from search.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerRefdomainsRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("history", history)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "refdomains", request, SiteExplorerRefdomainsResponse, exclude_none=True)

    def site_explorer_refdomains_history(
        self,
        request: SiteExplorerRefdomainsHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerRefdomainsHistoryResponse:
        """
        Refdomains history.

        Args:
            request: SiteExplorerRefdomainsHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerRefdomainsHistoryResponse containing SiteExplorerRefdomainsHistoryData:
                date (str)
                refdomains (int): (5 units) The total number of unique domains linking to your target.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerRefdomainsHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "refdomains-history", request, SiteExplorerRefdomainsHistoryResponse, exclude_none=True)

    def site_explorer_top_pages(
        self,
        request: SiteExplorerTopPagesRequest | None = None,
        *,
        timeout: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        where: str | None = None,
        select: SelectStr | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
        country: CountryEnum | None = None,
        date_compared: DateStr | None = None,
        date: DateStr | None = None,
        volume_mode: VolumeModeEnum | None = None,
    ) -> SiteExplorerTopPagesResponse:
        """
        Top pages.

        Args:
            request: SiteExplorerTopPagesRequest
                timeout (int, optional): A manual timeout duration in seconds. Default: None.
                limit (int, optional): The number of results to return. Default: 1000.
                order_by (str, optional): A column to order results by. See response schema for valid column identifiers. Default: None.
                where (str, optional): Filter expression. See filter-syntax.md for syntax. Default: None.
                select (str, required): A comma-separated list of columns to return. See response schema for valid column identifiers.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                date_compared (str, optional): A date to compare metrics with in YYYY-MM-DD format. Default: None.
                date (str, required): A date to report metrics on in YYYY-MM-DD format.
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.

        Returns:
            SiteExplorerTopPagesResponse containing SiteExplorerTopPagesData:
                keywords (int | None): The total number of keywords that your target ranks for in the top 100 organic search results.
                keywords_diff (int): The change in keywords between your selected dates.
                keywords_diff_percent (int): The change in keywords between your selected dates, in percents.
                keywords_merged (int): The total number of keywords optimized for sorting.
                keywords_prev (int | None): The keyword your target ranks for on the comparison date.
                raw_url (str): The ranking page URL in encoded format.
                raw_url_prev (str | None): The ranking page URL on the comparison date in encoded format.
                referring_domains (int | None): (5 units) The number of unique domains linking to a page.
                status (StatusEnum): The status of a page: the new page that just started to rank ("left"), the lost page that disappeared from search results ("right"), or no change ("both").
                sum_traffic (int | None): (10 units) An estimation of the monthly organic search traffic that a page gets from all the keywords that it ranks for.
                sum_traffic_merged (int): (10 units) The traffic field optimized for sorting.
                sum_traffic_prev (int | None): (10 units) The traffic on the comparison date.
                top_keyword (str | None): The keyword that brings the most organic traffic to a page.
                top_keyword_best_position (int | None): The ranking position that a page holds for its top keyword.
                top_keyword_best_position_diff (int | None): The change in the top position between your selected dates.
                top_keyword_best_position_kind (BestPositionKindEnum | None): The kind of the top position: organic, paid or a SERP feature.
                top_keyword_best_position_kind_prev (BestPositionKindEnum | None): The kind of the top position on the comparison date.
                top_keyword_best_position_prev (int | None): The top position on the comparison date.
                top_keyword_best_position_title (str | None): The title displayed for the page in its top keyword's SERP.
                top_keyword_best_position_title_prev (str | None): The title displayed for the page in its top keyword's SERP on the comparison date.
                top_keyword_country (CountryEnum1 | None): The country in which a page ranks for its top keyword.
                top_keyword_country_prev (CountryEnum1 | None): The country in which a page ranks for its top keyword on the comparison date.
                top_keyword_prev (str | None): The keyword that brings the most organic traffic to a page on the comparison date.
                top_keyword_volume (int | None): (10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter.
                top_keyword_volume_prev (int | None): (10 units) The search volume on the comparison date.
                traffic_diff (int): The change in traffic between your selected dates.
                traffic_diff_percent (int): The change in traffic between your selected dates, in percents.
                ur (float | None): URL Rating (UR) shows the strength of your target page’s backlink profile on a 100-point logarithmic scale.
                url (str | None): The ranking page URL.
                url_prev (str | None): The ranking page URL on the comparison date.
                ... and 5 more fields. See SiteExplorerTopPagesData for all fields.
        """
        if request is None:
            _missing = [k for k, v in [("select", select), ("target", target), ("date", date)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerTopPagesRequest(**{k: v for k, v in [("timeout", timeout), ("limit", limit), ("order_by", order_by), ("where", where), ("select", select), ("protocol", protocol), ("target", target), ("mode", mode), ("country", country), ("date_compared", date_compared), ("date", date), ("volume_mode", volume_mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "top-pages", request, SiteExplorerTopPagesResponse, exclude_none=True)

    def site_explorer_total_search_volume_history(
        self,
        request: SiteExplorerTotalSearchVolumeHistoryRequest | None = None,
        *,
        volume_mode: VolumeModeEnum | None = None,
        top_positions: ViewForEnum | None = None,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        country: CountryEnum | None = None,
        protocol: ProtocolEnum | None = None,
        target: str | None = None,
        mode: ModeEnum | None = None,
    ) -> SiteExplorerTotalSearchVolumeHistoryResponse:
        """
        Total search volume history.

        Args:
            request: SiteExplorerTotalSearchVolumeHistoryRequest
                volume_mode (VolumeModeEnum, optional): The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Default: 'monthly'.
                top_positions (ViewForEnum, optional): The number of top organic search positions to consider when calculating total search volume. Default: 'top_10'.
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                country (CountryEnum, optional): A two-letter country code (ISO 3166-1 alpha-2). Default: None.
                protocol (ProtocolEnum, optional): The protocol of your target. Default: 'both'.
                target (str, required): The target of the search: a domain or a URL.
                mode (ModeEnum, optional): The scope of the search based on the target you entered. Default: 'subdomains'.

        Returns:
            SiteExplorerTotalSearchVolumeHistoryResponse containing SiteExplorerTotalSearchVolumeHistoryData:
                date (str)
                total_search_volume (int): (10 units) The total search volume of keywords for which your target ranks within the specified `top_positions` in the search results.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerTotalSearchVolumeHistoryRequest(**{k: v for k, v in [("volume_mode", volume_mode), ("top_positions", top_positions), ("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("country", country), ("protocol", protocol), ("target", target), ("mode", mode)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "total-search-volume-history", request, SiteExplorerTotalSearchVolumeHistoryResponse, exclude_none=True)

    def site_explorer_url_rating_history(
        self,
        request: SiteExplorerUrlRatingHistoryRequest | None = None,
        *,
        history_grouping: HistoryGroupingEnum | None = None,
        date_to: DateStr | None = None,
        date_from: DateStr | None = None,
        target: str | None = None,
    ) -> SiteExplorerUrlRatingHistoryResponse:
        """
        URL Rating history.

        Args:
            request: SiteExplorerUrlRatingHistoryRequest
                history_grouping (HistoryGroupingEnum, optional): The time interval used to group historical data. Default: 'monthly'.
                date_to (str, optional): The end date of the historical period in YYYY-MM-DD format. Default: None.
                date_from (str, required): The start date of the historical period in YYYY-MM-DD format.
                target (str, required): The target of the search: a domain or a URL.

        Returns:
            SiteExplorerUrlRatingHistoryResponse containing SiteExplorerUrlRatingHistoryData:
                date (str)
                url_rating (float): The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.
        """
        if request is None:
            _missing = [k for k, v in [("date_from", date_from), ("target", target)] if v is None]
            if _missing:
                raise ValueError(f"Missing required argument(s): {', '.join(_missing)}")
            request = SiteExplorerUrlRatingHistoryRequest(**{k: v for k, v in [("history_grouping", history_grouping), ("date_to", date_to), ("date_from", date_from), ("target", target)] if v is not None})  # pyright: ignore[reportArgumentType]
        return self._request("site-explorer", "url-rating-history", request, SiteExplorerUrlRatingHistoryResponse, exclude_none=True)

    # fmt: on
