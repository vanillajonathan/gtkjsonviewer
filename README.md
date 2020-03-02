GtkJsonView
===========
A simple JSON viewer written in GTK.

## Usage

### From a JSON file
```sh
python gtkjsonview.py test.json
```

### From an input stream
```sh
echo '[{"id":"1"}]' | python gtkjsonview.py
```

## Screenshot

![GtkJsonView](http://farm4.static.flickr.com/3529/3252639468_9c41d0e97f_o_d.png)

## Dependencies

* Python 3
* GTK module
* simplejson module

Install:
```sh
sudo pip install simplejson
```
