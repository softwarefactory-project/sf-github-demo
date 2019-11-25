def test_apache(host):
    if host.system_info.distribution in ["ubuntu", "debian"]:
        name = "apache2"
    else:
        name = "httpd"

    package = host.package(name)
    assert package.is_installed

    service = host.service(name)
    assert service.is_enabled
    assert service.is_running
