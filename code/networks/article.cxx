#encoding "utf-8"
#GRAMMAR_ROOT root 
#filter &AnyWord<kwtype="names">

root -> AnyWord<kwtype="names", h-reg1> interp (Fact.Name);
root -> "<" "p" ">" AnyWord<kwtype="names", h-reg2> interp (Fact.Name) "<"  interp (+Fact.Name);