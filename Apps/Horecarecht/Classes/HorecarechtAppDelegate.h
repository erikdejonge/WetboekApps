//
//  HorecarechtAppDelegate.h
//  Horecarecht
//
//  Created by rabshakeh on 9/24/09 - 12:06 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class HorecarechtViewController;

@interface HorecarechtAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    HorecarechtViewController *viewController;
    UINavigationController     *navigationController;	
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet HorecarechtViewController *viewController;

@end

