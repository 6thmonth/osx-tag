{
  "targets": [
    {
      "target_name": "osx_tag",
      "sources": [ "osx_tag.mm" ],
      "libraries": [ "Foundation.framework" ],
      "cflags": ["-fobjc-arc"],
      "include_dirs" : [
	    "<!(node -e \"require('nan')\")"
	  ]
    }
  ]
}
