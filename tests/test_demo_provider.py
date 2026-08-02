from src.discovery.demo_provider import DemoProvider


def test_demo_provider_loads_clusters():
    provider = DemoProvider()

    clusters = provider.get_clusters()

    assert len(clusters) == 5