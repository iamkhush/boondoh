from django.db import models

# Create your models here.
class notice_of_appearence(models.Model):
    doc_id = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=500)
    sec = models.CharField(max_length=50)
    F = models.CharField(max_length=50)
    offcial_recieve = models.CharField(max_length=50)
    firm__or_organisation = models.CharField(max_length=500)
    filled_on_behalf = models.CharField(max_length=500)
    office = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    attorney_first_name = models.CharField(max_length=500)
    attorney_last_name = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    location = models.ForeignKey('location')

    def __unicode__(self):
        return "Attorney %s %s " %(self.attorney_first_name,self.attorney_last_name)
    
         
class itc_cases(models.Model):
    invoice_number = models.CharField(max_length=500)
    matter = models.CharField(max_length=500)
    unfair_acts_in_notice = models.CharField(max_length=500)
    patent_numbers = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    complainants = models.CharField(max_length=500)
    respondants = models.CharField(max_length=500)
    alj = models.CharField(max_length=500)
    oui_attorney = models.CharField(max_length=500)
    gc_attorney = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    notice = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    phase = models.CharField(max_length=500)
    inv_term_date = models.CharField(max_length=500)
    publ_comm_options = models.CharField(max_length=500)
    rel_court_decisions = models.CharField(max_length=500)
    status_results = models.CharField(max_length=500)
    dispos = models.CharField(max_length=500)
    unfair_acts = models.CharField(max_length=500)
    notes_ris_rem = models.CharField(max_length=500)
    act_exp_rem_orders = models.CharField(max_length=500)
    exclusion = models.CharField(max_length=500)
    target_date = models.CharField(max_length=500)
    violation_final_due_date = models.CharField(max_length=500)
    beg_end_dates_of_hearing = models.CharField(max_length=500)
    
    def __unicode__(self):
        return "Case with invoice number %s " %(self.invoice_number)
    
class district_courts_and_judges(models.Model):
    judge_first_name = models.CharField(max_length=500)
    judge_middle_name = models.CharField(max_length=500)
    judge_last_name = models.CharField(max_length=500)
    birth_year = models.CharField(max_length=500)
    court_name = models.CharField(max_length=500)
    president_name = models.CharField(max_length=500)
    part_affliation_of_president = models.CharField(max_length=500)
    ABA_rating = models.CharField(max_length=500)
    senate_vote_date = models.CharField(max_length=500)
    commission_date = models.CharField(max_length=500)
    retirement = models.CharField(max_length=500)
    termination_date = models.CharField(max_length=500)

    def __unicode__(self):
        return "%s %s" %(self.judge_first_name,self.judge_last_name)

class location(models.Model):
    state = models.CharField(max_length=500)
    office = models.CharField(max_length=500)
    class Meta:
        unique_together = ('state', 'office')
