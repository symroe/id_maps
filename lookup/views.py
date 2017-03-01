from django.views.generic import TemplateView

from identifiers.models import Identifier


class LookupSingle(TemplateView):
    template_name = "lookup_single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        identifier = self.kwargs['identifier']
        others = Identifier.objects.filter(code=identifier).exclude(code="").exclude(code=None)
        # others = Identifier.objects.all()
        same_as = []
        for other in others:
            same_as += [(x.identifier.namespace, x.identifier.code)
                        for x in other.same_as.all()
                        if x.identifier.code != identifier
                        and x.identifier.code]

        context['data'] = {
            'identifier': identifier,
            'same_as': list(set(same_as)),
        }
        return context

class NamespaceView(TemplateView):
    template_name = "namespace_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        namespace = self.kwargs['namespace']

        context['data'] = {
            'namespace': namespace,
            'identifiers': Identifier.objects.filter(namespace=namespace).exclude(code="").exclude(code=None),
        }
        return context
