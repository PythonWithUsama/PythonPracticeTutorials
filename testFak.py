import faker
# # from faker import Faker
# # fakerName = Faker('hi_IN')
# fakerName = faker.Faker()
# # print(fakerName.name())
# print(fakerName.text())
#
# # print(testfaker)
import pandas as pd
fakern = faker.Faker()
data = [fakern.profile() for i in range(10)]
df = pd.DataFrame(data)
print(df)