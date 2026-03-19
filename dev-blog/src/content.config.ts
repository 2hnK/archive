import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articlesCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/articles" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.string(),
    date: z.date(),
    imageUrl: z.string().optional(),
    isFeatured: z.boolean().optional().default(false),
  })
});

export const collections = {
  'articles': articlesCollection,
};
