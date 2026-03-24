        # 2. 裁剪冗余后缀 (已关闭)
        # 允许输入如: http://127.0.0.1:5000/v1/chat/completions -> 裁剪为 -> http://127.0.0.1:5000/v1
        # redundant_suffixes = ["/chat/completions", "/completions", "/chat"]
        # for suffix in redundant_suffixes:
        #     if url.endswith(suffix):
        #         url = url[:-len(suffix)]
        #         url = url.rstrip('/') # 再次去除可能暴露出来的斜杠
        #         break
