import os,datetime
HTML_TEMPLATE = '''
<DOCTYPE html>
<html>
<head>
<title>{title}</title>
<body>
<p>Posted on : {date}</p>
<p>
{content}
</p>
<a href="index.html">Back to HOME</a>
</body>
</head>

</html>
'''

INDEX_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>My blog </title></head>
<body>
<h1>My blog</h1>
<ul?{link}</lu>
</body>

</html>

'''

def generatepage(postfile,output_dir):
    with open(postfile,'r') as f:
        lines = f.readlines()
        blogtitle = lines[0].strip()
        blogcontent = lines[1:]
        dateandtime  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M%S')
        htmlfomrate = HTML_TEMPLATE.format(title=blogtitle,date=dateandtime,content=blogcontent)
        post_name = os.path.splitext(os.path.basename(postfile))[0] + '.html'
        with open(os.path.join(output_dir,post_name),'w') as f:
            f.write(htmlfomrate)
        return post_name
    
def updateindex(postfiles,output_dire):
    links = ''
    for f in postfiles:
        post_path = os.path.splitext(os.path.basename(f))[0] + '.html'
        with open(f,'r') as fl:
            title = fl.readline().strip()
            links += f'<li><a href = "{post_path}" >{title}</a></li>'
        
    content = INDEX_TEMPLATE.format(link = links)
    with open(output_dire,'w') as f:
            f.write(content)
    

if __name__ == '__main__':
    posts = "D:\\Model\\my-blog\\myblog\\posts"
    output = "D:\\Model\\my-blog\\myblog\\output"
    hpageadd = "D:\\Model\\my-blog\\myblog\\index.html"

    post_files = [os.path.join(posts, f) for f in os.listdir(posts) if f.endswith('.txt')]

    for f in post_files:
        generatepage(f,output)
    
    updateindex(post_files,hpageadd)

    print("Blog updated successfully")
            





