# HExHTTP
Header Exploitation HTTP

*HTTP header behavior analysis tool*

### Beta version


## Usage

	usage: hexhttp.py [-h] [-u URL] [--full]
	
	-h, --help        show this help message and exit
	-u URL            URL to test [required]
	-f URL_FILE       URL file to test
	--full            To display full header
	-H CUSTOM_HEADER  Header HTTP custom
	--behavior, -b    activate a lighter version of verbose, highlighting interesting cache behavior


## Examples

![alt tag](https://github.com/c0dejump/HExHTTP/blob/main/static/example_1.png)
![alt tag](https://github.com/c0dejump/HExHTTP/blob/main/static/example_2.png)
![alt tag](https://github.com/c0dejump/HExHTTP/blob/main/static/poisoner.png)

## Features

- Server Error response checking
- Localhost header response analysis
- Methods response analysis
- CPDoS technique
- CND Analysis
- Web cache poisoning
- Technologies analysis (Ngninx - Envoy - Apache) [IP]


### Based on :
- YWH HTTP Header Exploitation: https://blog.yeswehack.com/yeswerhackers/http-header-exploitation/
- Cache Poisoning at Scale https://youst.in/posts/cache-poisoning-at-scale/
- Web Cache Entanglement: Novel Pathways to Poisoning https://portswigger.net/research/web-cache-entanglement
- Practical Web Cache Poisoning https://portswigger.net/research/practical-web-cache-poisoning
- Exploiting cache design flaws https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws
- Responsible denial of service with web cache poisoning https://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning
- https://cpdos.org/
- Cache poisoning https://github.com/Th0h0/autopoisoner 