package com.devarchive.article;

import java.util.List;

public record TopicCategory(String name, int count, List<TopicSubcategory> subcategories) {
}
