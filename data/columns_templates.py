def getColumnsNames(template):
    if template == 'CUSTOMERS':
        return(CUSTOMERS)
    elif template == 'INTERMEDIARY_POLICY_LINK':
        return(INTERMEDIARY_POLICY_LINK)
    elif template == 'PRODUCT_SOURCE_TYPE':
        return(PRODUCT_SOURCE_TYPE)
    elif template == 'CUSTOMER_POLICY_LINK':
        return(CUSTOMER_POLICY_LINK)
    elif template == 'INTERMEDIARIES':
        return(INTERMEDIARIES)
    elif template == 'INTERMEDIARY_TYPE':
        return(INTERMEDIARY_TYPE)
    elif template == 'OPERATIONS':
        return(OPERATIONS)
    elif template == 'PARTY_ROLE':
        return(PARTY_ROLE)
    elif template == 'POLICIES':
        return(POLICIES)
    elif template == 'POLICY_STATUS':
        return(POLICY_STATUS)
    elif template == 'COUNTRY':
        return(COUNTRY)
    elif template == 'PRODUCT':
        return(PRODUCT)
    elif template == 'TRANSACTIONS':
        return(TRANSACTIONS)

'''
class ColumnNames:
    intermediaryType = ['INTERMEDIARY_TYPE_CODE',
'INTERMEDIARY_TYPE_DESC',
'LAST_UPDATED_TIMESTAMP']
    customerPolicyLink = ['POLICY_ID', 'CUSTOMER_ID', 'PARTY_ROLE_CODE', 'PARTY_RELATIONSHIP', 'FROM_DATE', 'TO_DATE', 'IS_PAYOR']
'''


CUSTOMERS = ['RUN_TIMESTAMP',
'CUSTOMER_ID',
'VERSION_ID',
'ORGUNIT_ID',
'ORGUNIT_CODE',
'CUSTOMER_SOURCE_REF_ID',
'CUSTOMER_SOURCE_UNIQUE_ID',
'CUSTOMER_NAME',
'COUNTRY_OF_RESIDENCE',
'COUNTRY_OF_ORIGIN',
'NATIONALITY_CODE',
'CUSTOMER_TYPE_CODE',
'CUSTOMER_STATUS_CODE',
'LAST_UPDATED_TIMESTAMP',
'PERSON_TITLE',
'FIRST_NAME',
'MIDDLE_NAMES',
'LAST_NAME',
'SUFFIX',
'COMPANY_NAME',
'COMPANY_FORM',
'REGISTERED_NUMBER',
'INCORPORATION_DATE',
'INCORPORATION_COUNTRY_CODE',
'BUSINESS_TYPE',
'BUSINESS_SEGMENT_1',
'BUSINESS_SEGMENT_2',
'INITIALS',
'DATE_OF_BIRTH',
'NAME_OF_BIRTH',
'FULL_ADDRESS',
'ADDRESS',
'CITY',
'ZONE',
'POSTAL_CODE',
'PLACE_OF_BIRTH',
'GENDER_CODE',
'PRIME_BRANCH_ID',
'RELATIONSHIP_MGR_ID',
'EMPLOYEE_FLAG',
'EMPLOYEE_NUMBER',
'MARITAL_STATUS',
'OCCUPATION',
'EMPLOYMENT_STATUS',
'ACQUISITION_DATE',
'CANCELLED_DATE',
'CUSTOMER_SEGMENT_1',
'CUSTOMER_SEGMENT_2',
'CUSTOMER_SEGMENT_3',
'RESIDENCE_FLAG',
'SPECIAL_ATTENTION_FLAG',
'DECEASED_FLAG',
'DORMANT_OVERRIDE_DATE',
'RISK_SCORE',
'BANKRUPT_FLAG',
'COMPENSATION_REQD_FLAG',
'CUSTOMER_COMPLAINT_FLAG',
'END_RELATIONSHIP_FLAG',
'MERCHANT_NUMBER',
'FACE_TO_FACE_FLAG',
'CHANNEL',
'AGE',
'NEAR_BORDER_FLAG',
'INTENDED_PRODUCT_USE',
'SOURCE_OF_FUNDS',
'COMPLEX_STRUCTURE',
'EXPECTED_ANNUAL_TURNOVER',
'TRADING_DURATION',
'BALANCE_SHEET_TOTAL',
'VAT_NUMBER',
'TAX_NUMBER',
'BROKER_CODE',
'BLACK_LISTED_FLAG',
'COMMENTS',
'TOTAL_DEPOSITS_BASE',
'TOTAL_LOANS_BASE',
'CURRENCY_CODE_BASE',
'WIRE_IN_NUMBER',
'WIRE_OUT_NUMBER',
'WIRE_IN_VOLUME',
'WIRE_OUT_VOLUME',
'CASH_IN_VOLUME',
'CASH_OUT_VOLUME',
'CHECK_IN_VOLUME',
'CHECK_OUT_VOLUME',
'OVERALL_SCORE_ADJUSTMENT',
'FP_WLM',
'FP_WLM_TIMESTAMP',
'DOMAIN_ID',
'CUSTOMER_CATEGORY_CODE',
'OWN_AFFILIATE_FLAG',
'MARKETING_SERVICE_LEVEL',
'FP_CUSTOMER',
'TAX_NUMBER_ISSUED_BY',
'FP_CDD',
'SANCTIONED_FLAG_INGESTED',
'PEP_FLAG_INGESTED',
'PEP_TYPE_INGESTED',
'PEP_RELATED_FLAG_INGESTED',
'RCA_FLAG_INGESTED',
'ADDRESS_VALID_FROM',
'ADDRESS_VALID_TO',
'EMAIL',
'EMAIL_VALID_FROM',
'EMAIL_VALID_TO',
'PHONE_AREA_CODE',
'PHONE_COUNTRY_CODE',
'PHONE_NUMBER',
'PHONE_EXTENSION',
'PHONE_VALID_FROM',
'PHONE_VALID_TO',
'ALTERNATE_NAME',
'TAX_NUMBER_TYPE',
'BUSINESS_CLASSIFICATION_CODE',
'BUSINESS_CLASSIFICATION_SYSTEM',
'CUSTOMER_CHANNEL_REMOTE_FLAG',
'FP_AAM']

INTERMEDIARY_POLICY_LINK = ['POLICY_ID',
'INTERMEDIARY_ID',
'PARTY_ROLE_CODE',
'PARTY_RELATIONSHIP',
'FROM_DATE',
'TO_DATE',
'LAST_UPDATED_TIMESTAMP']

INTERMEDIARY_TYPE = ['INTERMEDIARY_TYPE_CODE',
'INTERMEDIARY_TYPE_DESC',
'LAST_UPDATED_TIMESTAMP']

OPERATIONS = ['RunTimestamp',
'OperationSourceUniqueID',
'OperationSourceRefID',
'PolicySourceUniqueID',
'CustomerSourceUniqueID',
'IntermediarySourceUniqueID',
'BranchID',
'TxnTypeCode',
'TxnChannelCode',
'TxnAmountBase',
'CurrencyCodeBase',
'TxnAmountOrig',
'CurrencyCodeOrig',
'CreditDebitCode',
'PaymentMethod',
'Iban',
'Bic',
'AccountNumber',
'ForeignFlag',
'SourceOfFundsFlag',
'UnusualPaymentMethodFlag',
'ReimbursmentFlag',
'ProgrammedFlag',
'RejectedFlag',
'BeneficiaryClause',
'OrgUnitCode']

PARTY_ROLE = ['PARTY_ROLE_CODE',
'PARTY_ROLE_DESC',
'LAST_UPDATED_TIMESTAMP']

POLICIES = ['RunTimestamp',
'PolicySourceUniqueID',
'PolicySourceRefID',
'PrimaryCustomerID',
'CustomerSourceRefID',
'PolicyHolderName',
'PolicyCoHolderName',
'PolicyInsuredName',
'PolicyPayorName',
'IntermediarySourceUniqueID',
'IntermediarySourceRefID',
'IntermediaryName',
'BranchID',
'BranchName',
'ProductSourceTypeCode',
'ProductSourceTypeDesc',
'PolicyStatusCode',
'PolicyDuration',
'CountryCode',
'CurrencyCode',
'BeneficiaryClause',
'BeneficiaryClauseLastUpdate',
'SubscriptionDate',
'EffectiveDate',
'SurrenderDate',
'InitialAmount',
'InstallmentFrequency',
'PolicyValueToDate',
'SurrenderValueToDate',
'NonAmortizedAmountToDate',
'LastValueDate',
'TotalDepositToDate',
'TotalWithdrawalToDate',
'TotalAdvanceToDate',
'TotalReimbursmentToDate',
'LastWithdrawalAmount',
'LastWithdrawalDate',
'LastAdvanceAmount',
'LastAdvanceDate',
'LastReimbursmentAmount',
'LastReimbursmentDate',
'LastSinglePremiumAmount',
'LastSinglePremiumDate',
'OrgUnitCode']

POLICY_STATUS = ['PolicyStatusCode',
'PolicyStatusDesc']

PRODUCT_SOURCE_TYPE = ['ProductSourceTypeCode',
'ProductSourceTypeDesc',
'ProductId']

CUSTOMER_POLICY_LINK = ['POLICY_ID', 'CUSTOMER_ID', 'PARTY_ROLE_CODE', 'PARTY_RELATIONSHIP', 'FROM_DATE', 'TO_DATE', 'IS_PAYOR']

INTERMEDIARIES = ['RUN_TIMESTAMP','INTERMEDIARY_ID','INTERMEDIARY_SOURCE_UNIQUE_ID','INTERMEDIARY_SOURCE_REF_ID','EMPLOYEE_ID','INTERMEDIARY_NAME','INTERMEDIARY_TYPE_CODE','ADDRESS','POSTAL_CODE','CITY','COUNTRY_CODE','PHONE_NUMBER','FAX_NUMBER','EMAIL_ADDRESS','TARGET_MARKET','FROM_DATE','TO_DATE','APPROVED_FROM','APPROVED_TO','RISK_LEVEL','RISK_SCORE','ORGUNIT_CODE','ORGUNIT_ID','LAST_UPDATED_TIMESTAMP']

COUNTRY = ['COUNTRY_CODE',
'COUNTRY_NAME',
'VERSION_ID',
'LAST_UPDATED_TIMESTAMP',
'ISO_CODE',
'CROOK_COUNTRY_FLAG',
'TAX_HAVEN_FLAG',
'HIGHRISK_FLAG',
'FATF_FLAG',
'NARCOTIC_FLAG',
'OFAC_FLAG',
'SUSPICIOUS_FLAG',
'EUROPE_FLAG',
'TERRORISTHAVEN_FLAG',
'CONTINENT_NAME',
'REGION_CODE',
'NO_EXTERNAL_ACCESS',
'FRDDC_RISK',
'PF_RISK',
'AMLCB_RISK_FLAG',
'PFCD_RISK']

PRODUCT = ['ProductId', 'ProductName', 'ProductGroup', 'ProductClass', 'ProductLine']
TRANSACTIONS = ['RunTimestamp',
'SourceTxnUniqueId',
'SourceTxnNum',
'AccountSourceUniqueId',
'AccountSourceRefId',
'CustomerSourceUniqueId',
'PrimaryCustSrceRefId',
'BranchId',
'TxnSourceTypeCode',
'OwnAccountTransfer',
'CurrencyCodeOrig',
'CurrencyCodeBase',
'OriginationDate',
'PostingDate',
'ValueDate',
'SystemTimestamp',
'LocalTimestamp',
'ProductSourceTypeCode',
'TxnVolume',
'DeviceId',
'TxnAmountOrig',
'TxnAmountBase',
'CreditDebitCode',
'TransRefDesc',
'TransRefDesc2',
'TransRefDesc3',
'TransRefDesc4',
'TransRefDesc5',
'TransRefDesc6',
'ClientDePassage',
'TxnStatusCode',
'TxnChannelCode',
'SourceSystemCode',
'ErrorCorrectFlag',
'TransactionLocation',
'OrgUnitCode',
'TxnUsrDtls',
'DvcPosEntryMode',
'PinVerifyCd',
'CardId',
'EmployeeId',
'CounterPartyName',
'CounterPartyAddress',
'CounterPartyZone',
'CounterPartyPostalCode',
'CounterPartyCity',
'CounterPartyCountryCode',
'CounterPartyAccountNum',
'CounterPartyAccountName',
'CounterPartyAccountType',
'CounterPartyAccountIban',
'CounterPartyAccountBic',
'CounterPartyBankName',
'CounterPartyBankCode',
'CounterPartyBankAddress',
'CounterPartyBankCity',
'CounterPartyBankZone',
'CounterPartyBankPostalCode',
'CounterPartyBnkCntryCd',
'OriginatorName',
'BeneficiaryName',
'OriginatorBankName',
'BeneficiaryBankName',
'TellerId',
'CardSourceRefId',
'CheckNumber',
'CheckAccountNumber',
'CheckAmount',
'CashbackAMT']