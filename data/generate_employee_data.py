"""Generate a synthetic HR dataset (IBM HR-Analytics style schema, 1,470 employees).
Replace data/employee_data.csv with the real IBM HR CSV if your course provides one;
the notebook only relies on the columns listed in FEATURES."""
import numpy as np, pandas as pd
rng = np.random.default_rng(42)
N = 1470
grp = rng.choice(4, size=N, p=[.30, .22, .28, .20])  # hidden profiles (never given to the models)
dept = rng.choice(['Research & Development', 'Sales', 'Human Resources'], size=N, p=[.65, .30, .05])
def pick(*arrs): return np.select([grp==0, grp==1, grp==2, grp==3], arrs)
age = pick(rng.normal(38,6,N), rng.normal(35,7,N), rng.normal(26,3,N), rng.normal(49,5,N)).clip(19, 60).round()
level = pick(rng.choice([2,3,4,5],N,p=[.2,.35,.3,.15]), rng.choice([1,2,3,4],N,p=[.25,.4,.25,.1]),
             rng.choice([1,2],N,p=[.7,.3]), rng.choice([2,3,4],N,p=[.35,.45,.2]))
income = (2200 + level*2600 + (age-20)*55 + rng.normal(0,900,N)).clip(1500, 20000).round(-1)
tot_years = (age-21 + rng.normal(0,2,N)).clip(0, 40).round()
yrs_co = pick(rng.normal(8,3,N), rng.normal(5,3,N), rng.normal(1.8,1.2,N), rng.normal(18,4,N))
yrs_co = np.minimum(yrs_co.clip(0, 35), tot_years).round()
since_promo = pick(rng.normal(1.5,1.2,N), rng.normal(3.5,2,N), rng.normal(.8,.8,N), rng.normal(9,3,N)).clip(0, 15)
since_promo = np.minimum(since_promo, yrs_co).round()
ot = rng.random(N) < pick(.15, .85, .25, .10)
def sat(m): return np.clip(np.round(rng.normal(m, .8, N)), 1, 4).astype(int)
job_sat = pick(sat(3.5), sat(1.9), sat(2.8), sat(2.3))
env_sat = pick(sat(3.3), sat(2.1), sat(2.8), sat(2.6))
wlb = pick(sat(3.2), sat(1.8), sat(2.9), sat(2.8))
perf = pick(rng.choice([3,4,5],N,p=[.25,.5,.25]), rng.choice([2,3,4],N,p=[.3,.55,.15]),
            rng.choice([2,3,4],N,p=[.25,.6,.15]), rng.choice([2,3],N,p=[.55,.45]))
dist = np.clip(rng.gamma(2.0, 5, N), 1, 29).round()
train = pick(rng.poisson(3.3,N), rng.poisson(2,N), rng.poisson(2.8,N), rng.poisson(1.6,N)).clip(0, 6)
# attrition = noisy logistic function of observable drivers (not of the hidden profile)
z = (-1.6 + 1.5*ot - 0.55*(job_sat-2.5) - 0.45*(wlb-2.5) - 0.25*(env_sat-2.5) + 0.12*since_promo
     - 0.00012*income + 0.025*np.maximum(dist-15, 0) - 0.04*yrs_co + rng.normal(0, .5, N))
attr = rng.random(N) < 1/(1+np.exp(-z))
df = pd.DataFrame({'EmployeeID': np.arange(1, N+1), 'Age': age.astype(int), 'Department': dept, 'JobLevel': level,
    'MonthlyIncome': income.astype(int), 'TotalWorkingYears': tot_years.astype(int), 'YearsAtCompany': yrs_co.astype(int),
    'YearsSinceLastPromotion': since_promo.astype(int), 'DistanceFromHome': dist.astype(int),
    'OverTime': np.where(ot, 'Yes', 'No'), 'JobSatisfaction': job_sat, 'EnvironmentSatisfaction': env_sat,
    'WorkLifeBalance': wlb, 'PerformanceRating': perf, 'TrainingTimesLastYear': train.astype(int),
    'Attrition': np.where(attr, 'Yes', 'No')})
df.to_csv('data/employee_data.csv', index=False)
print(df.shape, 'attrition rate:', round((df.Attrition=='Yes').mean(), 3))
