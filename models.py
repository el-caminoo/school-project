from django.db import models


class Company(models.Model):
    first_name = models.CharField(max_length=22)
    last_name = models.CharField(max_length=33)
    DOB = models.DateField(blank=True, null=True)

    Nigeria = 'NGN'
    Ghana = 'GHN'
    Liberia = 'LBR'
    Senegal = 'SNG'
    COUNTRY = (
        (Nigeria, 'Nigeria'),
        (Ghana, 'Ghana'),
        (Liberia, 'Liberia'),
        (Senegal, 'Senegal')
    )
    country = models.CharField(max_length=99, choices=COUNTRY, default=Nigeria)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=22)

    MALE = 'M'
    FEMALE = 'F'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    sex = models.CharField(max_length=7, choices=SEX, default=MALE)

    D1 = 'D1'
    D2 = 'D2'
    D3 = 'D3'
    DURATION = (
        (D1, 'A month'),
        (D2, 'Couple of months'),
        (D3, 'Over a year')
    )
    use_duration = models.CharField(max_length=22, choices=DURATION, default=D1)

    R1 = 'R1'
    R2 = 'R2'
    R3 = 'R3'
    SCALE = (
        (R1, '1-3(Poor)'),
        (R2, '4-7(Average)'),
        (R3, '8-10(Good)')
    )
    product_rating = models.CharField(max_length=22, choices=SCALE, default=R1)

    COST = 'C'
    QUALITY = 'Q'
    COST_QUALITY = (
        (COST, 'Cost'),
        (QUALITY, 'Quality')
    )
    cost_quality = models.CharField(max_length=6, choices=COST_QUALITY, default=COST)

    YES = 'Y'
    NO = 'N'
    CONTINUOUS_USE = (
        (YES, 'Yes'),
        (NO, 'No')
    )
    continuous_use = models.CharField(max_length=33, choices=CONTINUOUS_USE, default=YES)
    
    def __str__(self):
        return self.first_name + '\t' + self.last_name

