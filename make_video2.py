import re

with open('hero.svg', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all <image> tags with a single animated one
href_match = re.search(r'href="(data:image/[^"]+)"', content)
if not href_match:
    print("No image found")
    exit(1)
href = href_match.group(1)

# Remove all <image> tags and their inner <animate> tags
content = re.sub(r'<image.*?</image>', '', content, flags=re.DOTALL)
content = re.sub(r'<image[^>]*/>', '', content)

# Remove the <animate attributeName="opacity" values="1;1;0;0"...> which fades the whole group out
content = re.sub(r'<animate attributeName="opacity" values="1;1;0;0"[^>]+/>', '', content)

# Inject the animated image right after <g mask="url(#vmaskB)">\n      <g>
# Wait, <g mask="url(#vmaskB)"> might be hard to match with spaces.
# Let's just find <g mask="url(#vmaskB)"> and inject right after the next <g>
match = re.search(r'<g mask="url\(#vmaskB\)">(.*?<g>)', content, re.DOTALL)
if match:
    animated_image = f'''
        <image x="560" y="0" width="724" height="540" href="{href}" preserveAspectRatio="xMidYMid slice">
            <animateTransform attributeName="transform" type="translate" values="0,0; -15,10; 0,0" dur="8s" repeatCount="indefinite" additive="sum" />
            <animateTransform attributeName="transform" type="scale" values="1; 1.05; 1" dur="8s" repeatCount="indefinite" additive="sum" />
        </image>
    '''
    content = content.replace(match.group(0), match.group(0) + animated_image)
    
    with open('hero.svg', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Video animation applied!")
else:
    print("Mask group not found")

