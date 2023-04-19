import pandas as pd
from django.core.management.base import BaseCommand
from measurement.models import Measurement
import os

class Command(BaseCommand):
    help = 'Imports a CSV file into the Measurement model'

    def handle(self, *args, **kwargs):
        csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'measurements.csv')

        # Read the CSV file using Pandas
        data = pd.read_csv(csv_file_path)

        # Iterate through each row in the DataFrame and create a Measurement instance
        for index, row in data.iterrows():
            Measurement.objects.create(
                height=row['Height (cm)'],
                weight=row[' Weight (kgs)'],
                age=row[' Age'],
                waist=row[' Waist (cm)'],
        )


        self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {csv_file_path}'))
