class EventSignUpPageLocators(object):

    SHIFT_JOB_PATH = '//table//tbody//tr[1]//td[1]'
    SHIFT_DATE_PATH = '//table//tbody//tr[1]//td[2]'
    SHIFT_STIME_PATH = '//table//tbody//tr[1]//td[3]'
    SHIFT_ETIME_PATH = '//table//tbody//tr[1]//td[4]'
    VIEW_JOBS_PATH = '//table//tbody//tr[1]//td[4]'
    VIEW_SHIFTS_PATH = '//table//tbody//tr[1]//td[4]'
    EVENT_NAME = '//table//tbody//tr[1]//td[1]'
    UPCOMING_SHIFT_SECTION = 'html/body/div[2]/h3'
    SLOTS_REMAINING_PATH = '//table//tbody//tr[1]//td[5]'
    EVENT_JOB_NAME = '//table//tbody//tr[1]//td[1]'


    # search form locators
    START_DATE_FROM = 'from'
    START_DATE_TO = 'to'


    # search from locators for job
    SEARCH_JOB_NAME = 'job_name'
    JOB_START_DATE_FROM = 'job_from'
    JOB_START_DATE_TO = 'job_to'
    JOB_CITY = 'job_city'
    JOB_STATE = 'job_state'
    JOB_COUNTRY = 'job_country'
    SEARCH_JOB_SUBMIT_PATH = 'submit_job'


    # Two choices depending on whether volunteer or admin
    ASSIGN_SHIFTS_PATH = '//table//tbody//tr[1]//td[4]'
    SHIFT_SIGNUP_PATH = '//table//tbody//tr[1]//td[4]'

    INFO_BOX = 'alert-info'
    DANGER_BOX = 'alert-danger'
    SUBMIT_PATH = '//form[1]'

    SHIFT_SIGNUP_PAGE = '//div[1]//div[1]//div[2]//ul[1]//li[3]'

