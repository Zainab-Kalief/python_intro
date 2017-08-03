def tupleInListFrom(dic):
    values = [];

    for key,val in dic.iteritems():
        new = ()
        new += (key,val,)
        values.append(new)

    print values

tupleInListFrom({
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
});
