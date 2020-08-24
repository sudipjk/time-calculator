def final_repr(final_hour,final_min,start_status,no_of_days,day):
  s=""
  if final_hour==0:
    s+="12:"
  else:
    s+=str(final_hour)+":"
  
  #if single digit minutes then append 0 to it
  if len(str(final_min))==1:
    s+="0"+str(final_min)+" "
  else:
    s+=str(final_min)+" "
  s+=start_status

  #optional argument i.e day not given
  if day=="option":
    if no_of_days>1:
      s+=" "+"("+str(no_of_days)+" "+"days later)"
    elif no_of_days==1:
      s+=" "+"(next day)"
  else:
    #optional argument i.e day given
    if no_of_days==0:
      s+=", "+day
    else:
      l=["Monday","tuesday","Wednesday","Thursday","Friday","saturDay","Sunday"]
      #finding day number of given day
      index=l.index(day)
      if no_of_days==1:
        s+=", "+l[index+1]+" "+"(next day)"
      else:
        #if number of days is greater than 1 finding the #weekday
        index=(index+no_of_days)%len(l)
        s+=", "+l[index]+" "+"("+str(no_of_days)+" "+"days later)"
  
  return s
  



def add_time(start, duration,day="option"):
    import math
    start_time,start_status=start.split()
    start_hour,start_min=start_time.split(":")
    duration_hour,duration_min=duration.split(":")
    start_hour=int(start_hour)
    start_min=int(start_min)
    duration_hour=int(duration_hour)
    duration_min=int(duration_min)
    final_hour=0
    final_min=0
    #finding sum of minutes
    final_min=(start_min+duration_min)%60
    #if sum is greater than 60 adding 1 hour to start time
    if start_min+duration_min>=60:
      start_hour+=1
    no_of_days=0
    #calculating number of days
    if duration_hour//24 !=0:
      no_of_days=(duration_hour//24)
    #finding remaining hours of the duration 
    #example duration=466 then duration=10
    duration_hour%=24
    #if sum leads to next day
    if start_hour+duration_hour>=12 and start_status=="PM":
      no_of_days+=1
    final_hour=(start_hour+duration_hour)%12
    #changing the time status
    if start_hour+duration_hour>=12 and start_hour+duration_hour<24:
      if start_status=="AM":
        start_status="PM"
      else:
        start_status="AM"

    return final_repr(final_hour,final_min,start_status,no_of_days,day)