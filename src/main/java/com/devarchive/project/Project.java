package com.devarchive.project;

import java.util.List;

public record Project(
		String slug,
		String title,
		String description,
		List<String> tags,
		String year,
		String image,
		String video,
		String archivalNote,
		String content
) {
	public String url() {
		return "/project/" + slug;
	}
}
