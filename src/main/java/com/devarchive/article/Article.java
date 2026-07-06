package com.devarchive.article;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;

public record Article(
		String slug,
		String title,
		String description,
		String category,
		String subcategory,
		LocalDate date,
		String timestamp,
		String imageUrl,
		boolean featured,
		String body,
		String html,
		String snippet,
		List<Heading> headings
) {
	private static final DateTimeFormatter DATE_LABEL = DateTimeFormatter.ofPattern("yyyy-MM-dd");
	private static final DateTimeFormatter KOREAN_DATE = DateTimeFormatter.ofPattern("yyyy. MM. dd.");

	public String url() {
		return "/articles/" + slug;
	}

	public String dateLabel() {
		return date.format(DATE_LABEL);
	}

	public String koreanDate() {
		return date.format(KOREAN_DATE);
	}
}
