from django.db import models


class SalarySlip(models.Model):
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    employee_name = models.CharField(
        max_length=100,
        verbose_name='Employee Name'
    )
    gross_pay = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name='Gross Pay'
    )

    class Meta:
        verbose_name = 'Salary Slip'
        verbose_name_plural = 'Salary Slips'
        ordering = ['employee_name']

    def __str__(self):
        return '{0}/{1}'.format(self.id, self.employee_name)
