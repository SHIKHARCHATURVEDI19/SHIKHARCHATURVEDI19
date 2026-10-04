import re

with open('hero.svg', 'r', encoding='utf-8') as f:
    content = f.read()

# The images are inside <g mask="url(#vmask)"><g mask="url(#vmaskB)"><g>
# Let's find that group and replace all its contents with a single floating, zooming image.

group_start = '<g mask="url(#vmask)"><g mask="url(#vmaskB)">\n      <g>'
if group_start in content:
    # Find the end of this group
    parts = content.split(group_start)
    before = parts[0] + group_start
    rest = parts[1]
    
    # Find the end of the <g>
    # The end of the images is marked by </image> and then </g>
    
    end_images = rest.find('</g>')
    images_block = rest[:end_images]
    after = rest[end_images:]
    
    # Extract the href from the first image
    href_match = re.search(r'href="(data:image/[^"]+)"', images_block)
    href = href_match.group(1) if href_match else ''
    
    animated_image = f'''
        <image x="560" y="0" width="724" height="540" href="{href}" preserveAspectRatio="xMidYMid slice">
            <animateTransform attributeName="transform" type="translate" values="0,0; -10,0; 0,0" dur="6s" repeatCount="indefinite" additive="sum" />
            <animateTransform attributeName="transform" type="scale" values="1; 1.05; 1" dur="6s" repeatCount="indefinite" additive="sum" />
        </image>
    '''
    
    new_content = before + animated_image + after
    with open('hero.svg', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Hero animation added!")
else:
    print("Group not found")

