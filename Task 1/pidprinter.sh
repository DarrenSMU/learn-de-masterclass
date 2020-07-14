pgrep -u root -l | awk '{print ""$1" root "$2""}'
