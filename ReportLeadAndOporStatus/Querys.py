# Diccionario de Querys utilizadas por el Script ReportLeadAndOporStatus.py

class Querys:

    sql={}

    #LEADS

    sql["LMercado"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON \
                        (leadid=vtiger_crmentity.crmid)\
                        WHERE vtiger_crmentity.deleted=0 AND converted=0"

    sql["LContactados"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                            WHERE vtiger_crmentity.deleted=0\
                            AND converted=0\
                            AND leadstatus='Contacted'"

    sql["LNoContactados"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                              WHERE vtiger_crmentity.deleted=0\
                              AND converted=0\
                              AND leadstatus='Not Contacted'"

    sql["LIntentandoContactar"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                                    WHERE vtiger_crmentity.deleted=0\
                                    AND converted=0\
                                    AND leadstatus='Attempted to Contact'"

    sql["LCold"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                      WHERE vtiger_crmentity.deleted=0\
                      AND converted=0\
                      AND leadstatus='Cold'"

    sql["LContactFuture"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                              WHERE vtiger_crmentity.deleted=0\
                              AND converted=0\
                              AND leadstatus='Contact in Future'"

    sql["LHot"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                    WHERE vtiger_crmentity.deleted=0\
                    AND converted=0\
                    AND leadstatus='Hot'"

    sql["LJunk"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                      WHERE vtiger_crmentity.deleted=0\
                      AND converted=0\
                      AND leadstatus='Junk Lead'"

    sql["LPreQualified"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                          WHERE vtiger_crmentity.deleted=0\
                          AND converted=0\
                          AND leadstatus='Pre Qualified'"

    sql["LQualified"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                              WHERE vtiger_crmentity.deleted=0\
                              AND converted=0\
                              AND leadstatus='Qualified'"

    sql["LWarm"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                                  WHERE vtiger_crmentity.deleted=0\
                                  AND converted=0\
                                  AND leadstatus='Warm'"

    sql["LLost"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                                      WHERE vtiger_crmentity.deleted=0\
                                      AND converted=0\
                                      AND leadstatus='Lost Lead'"

    sql["LWaitResponse"] = "SELECT count(*) FROM vtiger_leaddetails JOIN vtiger_crmentity ON (leadid=vtiger_crmentity.crmid)\
                                          WHERE vtiger_crmentity.deleted=0\
                                          AND converted=0\
                                          AND leadstatus='Esperando respuesta'"

    # POTENTIALS

    sql["OMercado"] = "SELECT count(*) FROM vtiger_potential JOIN vtiger_crmentity ON \
                        (potentialid=vtiger_crmentity.crmid)\
                        WHERE vtiger_crmentity.deleted=0 \
                        AND vtiger.vtiger_potential.converted = 0"

    sql["ODormidas"] = "SELECT count(*) FROM vtiger_potential JOIN vtiger_crmentity ON \
                            (potentialid=vtiger_crmentity.crmid)\
                             WHERE vtiger_crmentity.deleted=0 \
                             AND sales_stage='Oportunidad Dormida' AND vtiger.vtiger_potential.converted = 0"

    sql["ONegociando"] = "SELECT count(*) FROM vtiger_potential JOIN vtiger_crmentity ON \
                            (potentialid=vtiger_crmentity.crmid)\
                            WHERE vtiger_crmentity.deleted=0 \
                            AND sales_stage='Negotiation/Review' AND vtiger.vtiger_potential.converted = 0"

    sql["OCerradasWon"] = "SELECT count(*) FROM vtiger_potential JOIN vtiger_crmentity ON \
                            (potentialid=vtiger_crmentity.crmid)\
                            WHERE vtiger_crmentity.deleted=0 \
                            AND sales_stage='Closed Won' AND vtiger.vtiger_potential.converted = 0"

    sql["OCerradasLost"] = "SELECT count(*) FROM vtiger_potential JOIN vtiger_crmentity ON \
                            (potentialid=vtiger_crmentity.crmid)\
                            WHERE vtiger_crmentity.deleted=0\
                            AND sales_stage='Closed Lost' AND vtiger.vtiger_potential.converted = 0"