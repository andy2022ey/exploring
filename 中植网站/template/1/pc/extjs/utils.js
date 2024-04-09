// 中英文切换
function openurl(lmlink, wzlink, idx, constyle, curlang) {
    var newurl = "";

    if (idx == -1) { // 文章详情
        if (curlang == 'cn') { // 当前是中文，转英文
            if (constyle.indexOf('en-pc-site') != -1) { // 包括英文模板，相同页面转英文
                newurl = wzlink.replace("/cn/", "/en/");
            } else {
                newurl = "/en/";
            }
        } else {
            if (constyle.indexOf('cn-pc-site') != -1) { // 包括中文模板，相同页面转中文
                newurl = wzlink.replace("/en/", "/cn/");
            } else {
                newurl = "/";
            }
        }

    } else if (idx == -2) { // 无二级栏目
        if (curlang == 'cn') { // 当前是中文，转英文
            newurl = lmlink.replace("/cn/", "/en/");
        } else {
            newurl = lmlink.replace("/en/", "/cn/");
        }

    } else { // 有二级栏目
        if (curlang == 'cn') { // 当前是中文，转英文
            newurl = "".concat(lmlink.replace("/cn/", "/en/"), "?type=", idx);
        } else {
            newurl = "".concat(lmlink.replace("/en/", "/cn/"), "?type=", idx);
        }

    }

    window.open(newurl, "_self");
}