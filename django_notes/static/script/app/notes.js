Notes = Ember.Application.create({
  rootElement: '#ember'
});

Notes.Note = DS.Model.extend({
    title: DS.attr('string'),
    content_raw: DS.attr('string'),
    content_html: DS.attr('string')
    //tags: DS.hasMany('tag', { async: true })
});

Notes.Tag = DS.Model.extend({
    title: DS.attr('string')
});


Notes.Router.map(function() {
  this.resource("notes", function() {
    this.resource("note", { path : ":note_id" });
  });
  this.route("tags", { path : "/tags" });
  this.route("tag", { path : "/tags/:tag_id" });
});

Notes.NotesRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('note');
  },
});

Notes.TagsRoute = Ember.Route.extend({
  model: function() {
    return this.store.find('tag');
  }
});

Notes.NoteController = Ember.ObjectController.extend({});
Notes.TagController = Ember.ObjectController.extend({});

Notes.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
    namespace: 'api'
});
