
    def save (self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)