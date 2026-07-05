import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articlesCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/articles" }),
  schema: z.object({
    type: z.string().optional().default("Article"),
    title: z.string(),
    description: z.string(),
    category: z.string(),
    subcategory: z.string().optional(),
    date: z.date(),
    timestamp: z.string().optional(),
    imageUrl: z.string().optional(),
    isFeatured: z.boolean().optional().default(false),
  })
});

export const collections = {
  'articles': articlesCollection,
};
