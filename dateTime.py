from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 1
now = datetime.now()
print("Now:", now)

# 2
then = datetime(2001, 9, 11, 8, 46)
print("\nThen:", then)

# 3
diff = timedelta(weeks=3, days=5, hours=2, minutes=10, seconds=3)
print("\nTimedelta:", diff)

# 4
print("\nNow + diff:", now + diff)

# 5
print("\nDifference (now - then):", now - then)


# Timezone-aware datetimes
dt1 = datetime.now(ZoneInfo('Europe/Berlin'))
print("\nBerlin time:", dt1)

dt2 = datetime(2025, 6, 5, 12, tzinfo=ZoneInfo('US/Pacific'))
print("\nUS Pacific time:", dt2)

print("\nDifference between dt1 and dt2:", dt1 - dt2)