import os, json
from datetime import datetime, timedelta
from connectors._VKontakte import VKontakte
from json_files.access import access

date_from = datetime.strftime(datetime.today() - timedelta(days=1), "%Y-%m-%d")
date_to = datetime.strftime(datetime.today() - timedelta(days=1), "%Y-%m-%d")

client_name = "BRIDGESTONE"

client = json.load(open(os.path.join(os.path.split(os.getcwd())[0], "json_files\clients", "clients.json"), "r"))
vk_params = client[client_name].get('vkontakte', None)
access_token = access.VKONTAKTE_TOKEN_GENERAL

if vk_params:
    project = client[client_name]['bigquery']['project']
    path_to_bq = os.path.join(access.path_to_json,
                              access.name_json_files['project'][project]['path_to_bq'])

    for params in vk_params:
        report = VKontakte(access_token, params['account_id'], params['client_id'], client_name, path_to_bq, date_from,
                           date_to)
        campaigns_ids, campaigns_df = report.get_campaigns()
        campaign_ids_with_stat = report.report_campaigns_stat(campaigns_ids)
        ads_ids, ads_df = report.report_ads(campaign_ids_with_stat)
        report.report_ads_stat(ads_ids)
        report.report_demographics(ads_ids)
        report.report_post_reach(ads_df)
