from identifiers.models import Identifier, Relationship

IGNORE_VALUES = [
    "Not Applicable",
    "None"
    "*MISSING*"
]


def data_to_ids(data, namespace_prefix=""):
    for row in data:
        for key, value in row.items():
            if not value:
                continue
            if key in IGNORE_VALUES or value in IGNORE_VALUES:
                continue
            create_ids(value, key, relations=row)


def create_ids(identifier, namespace, relations=None):
    if identifier in IGNORE_VALUES:
        return
    main_identifier, _ = Identifier.objects.get_or_create(
        code=identifier,
        namespace=namespace,
    )
    if not relations:
        relations = {}
    for key, value in relations.items():
        if key == namespace and value == identifier:
            continue
        if not value:
            continue
        if key in IGNORE_VALUES or value in IGNORE_VALUES:
            continue

        value_identifier = create_ids(value, key)
        Relationship.objects.get_or_create(
            identifier=value_identifier,
            same_as=main_identifier)
    return main_identifier

def build_same_as(identifier, known):
    return [x.identifier for x in identifier.same_as.all().exclude(pk__in=[x.pk for x in known])]

def update_relationships():
    print("Updating relationships")
    for identifier in Identifier.objects.all():
        same_as_list = []
        for i in build_same_as(identifier, same_as_list):
            same_as_list += build_same_as(i, known=same_as_list)
        same_as_list = list(set(same_as_list))
        for i in same_as_list:
            Relationship.objects.get_or_create(
                identifier=i,
                same_as=identifier)

