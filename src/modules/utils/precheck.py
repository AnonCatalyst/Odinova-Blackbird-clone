from modules.utils.http_client import do_sync_request
import config


def perform_pre_check(precheck_params, headers):
    method = precheck_params["method"]
    url = precheck_params["endpoint"]
    data = precheck_params["data"]
    precheck_headers = precheck_params["headers"]
    response = do_sync_request(method, url, data, precheck_headers)
    if precheck_params["type"] == "cookie":
        cookie_name = precheck_params["cookie_name"]
        cookie_value = response.cookies.get(precheck_params["cookie_name"])
        if cookie_value:
            if config.verbose:
                config.console.print(
                    f"🔑 Acquired cookie {cookie_name}: {cookie_value}"
                )
            for header in headers:
                headers[header] = headers[header].replace(
                    "{" + cookie_name + "_value}", cookie_value
                )

    return headers
