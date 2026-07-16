package com.devarchive.web;

import java.util.List;

public record SkillGroup(String name, String description, List<Skill> skills) {
}
