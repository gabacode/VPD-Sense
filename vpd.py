def vpd(rh, temp):
    e = 2.71828
    svp = 610.78*(e**(temp/(temp+238.3)*17.2694))
    ksvp = svp/1000
    vpd = ksvp*(1-(rh/100))                     
    return "Relative Humidity:"+str(rh)+"%"+"\nTemperature:"+str(temp)+"C°"+"\nVPD:"+str(round(vpd, 2))+"kPa"
