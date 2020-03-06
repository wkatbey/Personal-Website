from django.db.models import Model

class PageSectionText(Model):
	value = models.TextField()
	col_length = models.IntegerField()

class PageSection(Model):
	heading = models.TextField()
	heading_icon = models.TextField()
	text = models.ManyToManyField(PageSectionText)

class HomePage(Model):
	intro = models.TextField()

	page_sections = models.ManyToManyField(PageSection)

class CurrentProject(Model):
	heading = models.TextField()
	heading_icon = models.TextField()

	tech_stack = models.TextField()
	description = models.TextField()

class CurrentProjectsSection(Model):
	projects = models.ManyToManyField(CurrentProject)