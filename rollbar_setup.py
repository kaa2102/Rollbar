import rollbar

rollbar.init(
  access_token='PROD_SERVER_ITEM_TOKEN'
  environment='testenv',
  code_version='1.0'
)
rollbar.report_message('Rollbar is configured correctly', 'info')
