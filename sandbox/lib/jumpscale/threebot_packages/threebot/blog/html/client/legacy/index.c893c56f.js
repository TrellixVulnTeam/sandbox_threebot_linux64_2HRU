import{a as t,b as a,c as e,d as s,i as n,s as o,e as r,S as u,R as p,w as c,x as i,y as m,r as l,A as g,t as f,j as h,q as d,P as b,n as P,B as $,E as v}from"./index.da608116.js";import{_ as j,d as x,b as L}from"./app.fecb3c59.js";import"./showdown.f97ad806.js";import{L as k}from"./ListPagination.bba15e93.js";import"./Tags.45b6ef89.js";import{P as N}from"./PostList.d4ca214b.js";function w(t){return{c:P,l:P,m:P,p:P,i:P,o:P,d:P}}function _(t){var a,e,s=new N({props:{posts:t.value,username:t.username}}),n=new k({props:{articlesCount:t.totalPostsLength,articlesPerPage:t.metadata.posts_per_page,objectPath:"/blog/"+t.username+"/posts",page:t.pageNum}});return{c:function(){s.$$.fragment.c(),a=c(),n.$$.fragment.c()},l:function(t){s.$$.fragment.l(t),a=m(t),n.$$.fragment.l(t)},m:function(t,o){$(s,t,o),l(t,a,o),$(n,t,o),e=!0},p:function(t,a){var e={};t.posts&&(e.posts=a.value),t.username&&(e.username=a.username),s.$set(e);var o={};t.totalPostsLength&&(o.articlesCount=a.totalPostsLength),t.metadata&&(o.articlesPerPage=a.metadata.posts_per_page),t.username&&(o.objectPath="/blog/"+a.username+"/posts"),t.pageNum&&(o.page=a.pageNum),n.$set(o)},i:function(t){e||(f(s.$$.fragment,t),f(n.$$.fragment,t),e=!0)},o:function(t){h(s.$$.fragment,t),h(n.$$.fragment,t),e=!1},d:function(t){v(s,t),t&&d(a),v(n,t)}}}function y(t){return{c:P,l:P,m:P,p:P,i:P,o:P,d:P}}function q(t){var a,e,s,n,o={ctx:t,current:null,token:null,pending:y,then:_,catch:w,value:"value",error:"null",blocks:[,,,]};return p(s=t.posts,o),{c:function(){a=c(),e=i(),o.block.c(),this.h()},l:function(t){a=m(t),e=i(),o.block.l(t),this.h()},h:function(){document.title="Blog"},m:function(t,s){l(t,a,s),l(t,e,s),o.block.m(t,o.anchor=s),o.mount=function(){return e.parentNode},o.anchor=e,n=!0},p:function(a,e){t=e,o.ctx=t,"posts"in a&&s!==(s=t.posts)&&p(s,o)||o.block.p(a,g(g({},t),o.resolved))},i:function(t){n||(f(o.block),n=!0)},o:function(t){for(var a=0;a<3;a+=1){var e=o.blocks[a];h(e)}n=!1},d:function(t){t&&(d(a),d(e)),o.block.d(t),o.token=null,o=null}}}function B(t){return C.apply(this,arguments)}function C(){return(C=j(x.mark(function t(a){var e,s,n,o,r,u,p,c,i,m,l,g,f;return x.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return a.host,e=a.path,s=a.params,n=a.query,console.log("params in posts index",JSON.stringify(s)),(o=parseInt(n.page))||this.redirect(302,"".concat(s.theuser,"/posts?page=1")),t.next=6,this.fetch("".concat(s.theuser,"/posts.json"));case 6:return r=t.sent,o>0&&o--,t.next=10,r.json();case 10:return u=t.sent,console.log(u.length),p=u.length,t.next=15,this.fetch("".concat(s.theuser,"/metadata.json"));case 15:return c=t.sent,t.next=18,c.json();case 18:return i=t.sent,m=i.posts_per_page||5,l=o*m,g=o*m+m,f=u.slice(l,g),t.abrupt("return",{path:e,posts:f,totalPostsLength:p,metadata:i});case 24:case"end":return t.stop()}},t,this)}))).apply(this,arguments)}function S(t,a,e){var s,n=a.posts,o=void 0===n?[]:n,r=a.metadata,u=a.totalPostsLength,p=a.path,c=L(),i=(c.preloading,c.page);c.session;b(t,i,function(t){e("$page",s=t)}),console.log("in posts index",s.params);var m=a.username,l=void 0===m?s.params.theuser:m,g=a.pageNum,f=void 0===g?s.query.page:g;return t.$set=function(t){"posts"in t&&e("posts",o=t.posts),"metadata"in t&&e("metadata",r=t.metadata),"totalPostsLength"in t&&e("totalPostsLength",u=t.totalPostsLength),"path"in t&&e("path",p=t.path),"username"in t&&e("username",l=t.username),"pageNum"in t&&e("pageNum",f=t.pageNum)},{posts:o,metadata:r,totalPostsLength:u,path:p,page:i,username:l,pageNum:f}}export default(function(p){function c(t){var u;return a(this,c),u=e(this,s(c).call(this)),n(r(u),t,S,q,o,["posts","metadata","totalPostsLength","path","username","pageNum"]),u}return t(c,u),c}());export{B as preload};