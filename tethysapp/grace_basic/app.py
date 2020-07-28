from tethys_sdk.base import TethysAppBase, url_map_maker


class GraceBasic(TethysAppBase):
    """
    Tethys app class for GRACE Basic.
    """

    name = 'GRACE Basic'
    index = 'grace_basic:home'
    icon = 'grace_basic/images/icon.gif'
    package = 'grace_basic'
    root_url = 'grace-basic'
    color = '#7a6fab'
    description = 'App for GRACE-Basic App Tutorial'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='grace-basic',
                controller='grace_basic.controllers.home'
            ),
            UrlMap(
                name='home_graph',
                url='grace-basic/home/{id}',
                controller='grace_basic.controllers.home_graph'
            ),
        )

        return url_maps