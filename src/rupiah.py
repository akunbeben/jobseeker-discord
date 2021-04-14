def format_rupiah(nominal):
    nominal = str(nominal)
    if len(nominal) <= 3:
        return 'Rp ' + nominal     
    else:
        p = nominal[-3:]
        q = nominal[:-3]
        return format_rupiah(q) + '.' + p