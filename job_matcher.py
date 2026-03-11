def match_resume_job(resume, job):

    resume_words = set(resume.lower().split())
    job_words = set(job.lower().split())

    matched = resume_words.intersection(job_words)

    score = int(len(matched) / len(job_words) * 100)

    return score, matched