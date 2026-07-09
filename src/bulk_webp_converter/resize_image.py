from constants import LS_MAX_WIDTH, PORT_MAX_WIDTH, SQ_MAX_WIDTH

def resize_img(src_image):
    
    aspect_ratio = src_image.height / src_image.width
    
    if (src_image.width > src_image.height):
        proportional_height = aspect_ratio * LS_MAX_WIDTH
        processed_image = src_image.resize((LS_MAX_WIDTH, round(proportional_height)),1)

    elif(src_image.width < src_image.height): 
        proportional_height = aspect_ratio * PORT_MAX_WIDTH
        processed_image = src_image.resize((PORT_MAX_WIDTH, round(proportional_height)),1)
        
    elif(src_image.width == src_image.height): 
        processed_image = src_image.resize((SQ_MAX_WIDTH, SQ_MAX_WIDTH),1)
    
    return processed_image

