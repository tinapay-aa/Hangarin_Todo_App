from django.core.management.base import BaseCommand
from todos.models import Task, Note, SubTask, TaskStatus, Category, Priority
from faker import Faker
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Creates random initial data'
    
    def handle(self, *args, **kwards):
        self.generate_tasks(10)
        self.generate_subtasks(10)
        self.generate_notes(5)
    
    def generate_tasks(self, count: int):
        fake = Faker()
        for _ in range(count):
            task = Task.objects.create(
                title = fake.sentence(nb_words=5),
                description = fake.paragraph(nb_sentences=3),
                deadline = timezone.make_aware(fake.date_time_this_month()),
                status = fake.random_element(elements=["Pending", "In Progress", "Completed"])
            )
            
            task.save()
        self.stdout.write(
            self.style.SUCCESS("Successfully created Tasks")
        )
    
    def generate_subtasks(self, count: int):
        fake = Faker()
        
        for _ in range(count):
            subtask = SubTask.objects.create(
                parent_task = Task.objects.order_by('?').first(),
                title = fake.sentence(nb_words=5),
                status = fake.random_element(elements=["Pending", "In Progress", "Completed"])
            )
            subtask.save()
            
        self.stdout.write(
            self.style.SUCCESS("Successfully created Sub-Tasks")
        )
        
    def generate_notes(self, count: int):
        fake = Faker()
        
        for _ in range(count):
            note = Note.objects.create(
                task = Task.objects.order_by('?').first(),
                content = fake.paragraph(nb_sentences=4),
            )
            note.save()
            
        self.stdout.write(
            self.style.SUCCESS("Successfully created notes")
        )